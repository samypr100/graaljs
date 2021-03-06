/*
 * Copyright (c) 2019, 2019, Oracle and/or its affiliates. All rights reserved.
 * DO NOT ALTER OR REMOVE COPYRIGHT NOTICES OR THIS FILE HEADER.
 *
 * The Universal Permissive License (UPL), Version 1.0
 *
 * Subject to the condition set forth below, permission is hereby granted to any
 * person obtaining a copy of this software, associated documentation and/or
 * data (collectively the "Software"), free of charge and under any and all
 * copyright rights in the Software, and any and all patent rights owned or
 * freely licensable by each licensor hereunder covering either (i) the
 * unmodified Software as contributed to or provided by such licensor, or (ii)
 * the Larger Works (as defined below), to deal in both
 *
 * (a) the Software, and
 *
 * (b) any piece of software and/or hardware listed in the lrgrwrks.txt file if
 * one is included with the Software each a "Larger Work" to which the Software
 * is contributed by such licensors),
 *
 * without restriction, including without limitation the rights to copy, create
 * derivative works of, display, perform, and distribute the Software and make,
 * use, sell, offer for sale, import, export, have made, and have sold the
 * Software and the Larger Work(s), and to sublicense the foregoing rights on
 * either these or other terms.
 *
 * This license is subject to the following condition:
 *
 * The above copyright notice and either this complete permission notice or at a
 * minimum a reference to the UPL must be included in all copies or substantial
 * portions of the Software.
 *
 * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 * IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 * FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 * AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 * LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
 * OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
 * SOFTWARE.
 */
package com.oracle.truffle.js.nodes.access;

import java.util.ArrayList;
import java.util.List;

import com.oracle.truffle.api.CompilerDirectives;
import com.oracle.truffle.api.dsl.Specialization;
import com.oracle.truffle.api.object.DynamicObject;
import com.oracle.truffle.api.profiles.ConditionProfile;
import com.oracle.truffle.js.nodes.JavaScriptBaseNode;
import com.oracle.truffle.js.runtime.Boundaries;
import com.oracle.truffle.js.runtime.JSContext;
import com.oracle.truffle.js.runtime.JSTruffleOptions;
import com.oracle.truffle.js.runtime.builtins.JSArray;
import com.oracle.truffle.js.runtime.builtins.JSClass;
import com.oracle.truffle.js.runtime.builtins.JSProxy;
import com.oracle.truffle.js.runtime.objects.JSObject;
import com.oracle.truffle.js.runtime.objects.JSShape;
import com.oracle.truffle.js.runtime.objects.PropertyDescriptor;

/**
 * EnumerableOwnPropertyNames (O, kind).
 */
public abstract class EnumerableOwnPropertyNamesNode extends JavaScriptBaseNode {

    private final boolean keys;
    private final boolean values;
    private final JSContext context;
    @Child private GetOwnPropertyNode getOwnPropertyNode;
    private final ConditionProfile hasFastShapesProfile = ConditionProfile.createBinaryProfile();

    protected EnumerableOwnPropertyNamesNode(JSContext context, boolean keys, boolean values) {
        this.context = context;
        this.keys = keys;
        this.values = values;
    }

    public static EnumerableOwnPropertyNamesNode createKeys(JSContext context) {
        return EnumerableOwnPropertyNamesNodeGen.create(context, true, false);
    }

    public static EnumerableOwnPropertyNamesNode createValues(JSContext context) {
        return EnumerableOwnPropertyNamesNodeGen.create(context, false, true);
    }

    public static EnumerableOwnPropertyNamesNode createKeysValues(JSContext context) {
        return EnumerableOwnPropertyNamesNodeGen.create(context, true, true);
    }

    public abstract List<? extends Object> execute(DynamicObject obj);

    @Specialization
    protected List<? extends Object> enumerableOwnPropertyNames(DynamicObject thisObj) {
        JSClass jsclass = JSObject.getJSClass(thisObj);
        if (hasFastShapesProfile.profile(keys && !values && JSTruffleOptions.FastOwnKeys && jsclass.hasOnlyShapeProperties(thisObj))) {
            return JSShape.getEnumerablePropertyNames(thisObj.getShape());
        } else {
            boolean isProxy = JSProxy.isProxy(thisObj);
            Iterable<Object> ownKeys = jsclass.ownPropertyKeys(thisObj);
            List<Object> properties = new ArrayList<>();
            for (Object key : ownKeys) {
                if (key instanceof String) {
                    PropertyDescriptor desc = getOwnProperty(thisObj, key);
                    if (desc != null && desc.getEnumerable()) {
                        if (keys && !values) {
                            Boundaries.listAdd(properties, key);
                        } else {
                            Object value = (desc.isAccessorDescriptor() || isProxy) ? jsclass.get(thisObj, key) : desc.getValue();
                            if (!keys && values) {
                                Boundaries.listAdd(properties, value);
                            } else {
                                assert keys && values;
                                Boundaries.listAdd(properties, JSArray.createConstant(context, new Object[]{key, value}));
                            }
                        }
                    }
                }
            }
            return properties;
        }
    }

    protected PropertyDescriptor getOwnProperty(DynamicObject thisObj, Object key) {
        if (getOwnPropertyNode == null) {
            CompilerDirectives.transferToInterpreterAndInvalidate();
            getOwnPropertyNode = insert(GetOwnPropertyNode.create(values, true, false, false));
        }
        return getOwnPropertyNode.execute(thisObj, key);
    }
}
