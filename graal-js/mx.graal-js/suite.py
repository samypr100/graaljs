suite = {
  "mxversion" : "5.127.1",

  "name" : "graal-js",

  "imports" : {
    "suites" : [
        {
           "name" : "tools",
           "subdir" : True,
           "version" : "8c629b91f1882a6d7e482832f87f99a9071a3a23",
           "urls" : [
                {"url" : "https://github.com/graalvm/graal.git", "kind" : "git"},
                {"url" : "https://curio.ssw.jku.at/nexus/content/repositories/snapshots", "kind" : "binary"},
            ]
        },
    ],
  },

  "repositories" : {
    "graaljs-binary-snapshots" : {
      "url": "https://curio.ssw.jku.at/nexus/content/repositories/snapshots",
      "licenses" : ["Oracle Proprietary"]
    },
  },

  "licenses" : {
    "Oracle Proprietary" : {
      "name" : "ORACLE PROPRIETARY/CONFIDENTIAL",
      "url" : "http://www.oracle.com/us/legal/copyright/index.html"
    }
  },

  "defaultLicense" : "Oracle Proprietary",

  "javac.lint.overrides" : "none",

  "libraries" : {
    "NETBEANS_PROFILER" : {
      "urls" : ["https://lafo.ssw.uni-linz.ac.at/pub/graal-external-deps/truffle/js/org-netbeans-lib-profiler-8.2-201609300101.jar"],
      "sha1" : "4b52bd03014f6d080ef0528865c1ee50621e35c6",
    },

    "ICU4J" : {
      "sha1" : "6f06e820cf4c8968bbbaae66ae0b33f6a256b57f",
      "maven" : {
        "groupId" : "com.ibm.icu",
        "artifactId" : "icu4j",
        "version" : "59.1",
      },
    },

    "TEST262" : {
      "sha1" : "0a879659eefc76edae39a1417f08a58c9a01f792",
      "urls" : ["https://lafo.ssw.uni-linz.ac.at/pub/graal-external-deps/truffle/js/test262-f3b5a1e.tar.bz2"],
    },

    "TESTNASHORN" : {
      "sha1" : "1a31d35e485247e0edf2738a248e1bc2b97f1054",
      "urls" : ["https://lafo.ssw.uni-linz.ac.at/pub/graal-external-deps/truffle/js/testnashorn-e118c818dbf8.tar.bz2"],
    },

    "TESTNASHORN_EXTERNAL" : {
      "sha1" : "3e3edc251d800bc74f28c78f75844c7086cb5216",
      "urls" : ["https://lafo.ssw.uni-linz.ac.at/pub/graal-external-deps/truffle/js/testnashorn-external-0f91116bb4bd.tar.bz2"],
    },

    "NASHORN_INTERNAL_TESTS" : {
      "sha1" : "b5840706cc8ce639fcafeab1bc61da2d8aa37afd",
      "urls" : ["https://lafo.ssw.uni-linz.ac.at/pub/graal-external-deps/truffle/js/nashorn-internal-tests-700f5e3f5ff2.jar"],
    },

    "TESTV8" : {
      "sha1" : "dd8107d045713ac6e880459ec7ae79531d23efb1",
      "urls" : ["https://lafo.ssw.uni-linz.ac.at/pub/graal-external-deps/truffle/js/testv8-20170906.tar.gz"],
    },

    "JACKSON_CORE" : {
      "sha1" : "2ef7b1cc34de149600f5e75bc2d5bf40de894e60",
      "maven" : {
        "groupId" : "com.fasterxml.jackson.core",
        "artifactId" : "jackson-core",
        "version" : "2.8.6",
      },
    },

    "JACKSON_ANNOTATIONS" : {
      "sha1" : "9577018f9ce3636a2e1cb0a0c7fe915e5098ded5",
      "maven" : {
        "groupId" : "com.fasterxml.jackson.core",
        "artifactId" : "jackson-annotations",
        "version" : "2.8.6",
      },
    },

    "JACKSON_DATABIND" : {
      "sha1" : "c43de61f74ecc61322ef8f402837ba65b0aa2bf4",
      "maven" : {
        "groupId" : "com.fasterxml.jackson.core",
        "artifactId" : "jackson-databind",
        "version" : "2.8.6",
      },
    },
  },

  "projects" : {
    "com.oracle.truffle.js.runtime" : {
      "subDir" : "src",
      "sourceDirs" : ["src"],
      "dependencies" : [
        "com.oracle.truffle.js.runtime.doubleconv",
        "com.oracle.truffle.regex",
        "mx:ASM_DEBUG_ALL",
        "ICU4J",
      ],
      "annotationProcessors" : ["truffle:TRUFFLE_DSL_PROCESSOR"],
      "javaCompliance" : "1.8",
      "workingSets" : "Truffle,JavaScript",
    },

    "com.oracle.truffle.js.nodes" : {
      "subDir" : "src",
      "sourceDirs" : ["src"],
      "dependencies" : [
        "com.oracle.truffle.js.runtime",
        "com.oracle.truffle.js.annotations",
        "com.oracle.truffle.js.codec",
      ],
      "checkstyle" : "com.oracle.truffle.js.runtime",
      "javaCompliance" : "1.8",
      "annotationProcessors" : ["truffle:TRUFFLE_DSL_PROCESSOR", "TRUFFLE_JS_FACTORY_PROCESSOR"],
      "workingSets" : "Truffle,JavaScript",
    },

    "com.oracle.truffle.js.builtins" : {
      "subDir" : "src",
      "sourceDirs" : ["src"],
      "dependencies" : ["com.oracle.truffle.js.nodes"],
      "checkstyle" : "com.oracle.truffle.js.runtime",
      "javaCompliance" : "1.8",
      "annotationProcessors" : ["truffle:TRUFFLE_DSL_PROCESSOR"],
      "workingSets" : "Truffle,JavaScript",
    },

    "com.oracle.truffle.js.parser" : {
      "subDir" : "src",
      "sourceDirs" : ["src"],
      "dependencies" : [
        "com.oracle.truffle.js.builtins",
        "com.oracle.js.parser",
      ],
      "checkstyle" : "com.oracle.truffle.js.runtime",
      "javaCompliance" : "1.8",
      "annotationProcessors" : ["truffle:TRUFFLE_DSL_PROCESSOR"],
      "workingSets" : "Truffle,JavaScript",
    },

    "com.oracle.js.parser" : {
      "subDir" : "src",
      "sourceDirs" : ["src"],
      "dependencies" : [
        "truffle:TRUFFLE_API",
      ],
      "javaCompliance" : "1.8",
      "annotationProcessors" : [],
      "workingSets" : "Truffle,JavaScript",
    },

    "com.oracle.truffle.js.shell" : {
      "subDir" : "src",
      "sourceDirs" : ["src"],
      "dependencies" : [
        "sdk:LAUNCHER_COMMON",
      ],
      "checkstyle" : "com.oracle.truffle.js.runtime",
      "javaCompliance" : "1.8",
      "workingSets" : "Truffle,JavaScript",
    },

    "com.oracle.truffle.js.annotations" : {
      "subDir" : "src",
      "sourceDirs" : ["src"],
      "dependencies" : [],
      "checkstyle" : "com.oracle.truffle.js.runtime",
      "javaCompliance" : "1.8",
      "workingSets" : "Truffle,JavaScript",
    },

    "com.oracle.truffle.js.codec" : {
      "subDir" : "src",
      "sourceDirs" : ["src"],
      "dependencies" : [],
      "checkstyle" : "com.oracle.truffle.js.runtime",
      "javaCompliance" : "1.8",
      "workingSets" : "Truffle,JavaScript",
    },

    "com.oracle.truffle.js.snapshot" : {
      "subDir" : "src",
      "sourceDirs" : ["src"],
      "dependencies" : [
        "com.oracle.truffle.js.parser",
      ],
      "checkstyle" : "com.oracle.truffle.js.runtime",
      "javaCompliance" : "1.8",
      "workingSets" : "Truffle,JavaScript",
    },

    "com.oracle.truffle.js.factory.processor" : {
      "subDir" : "src",
      "sourceDirs" : ["src"],
      "dependencies" : [
        "com.oracle.truffle.js.annotations",
        "com.oracle.truffle.js.codec",
        "truffle:TRUFFLE_API",
      ],
      "checkstyle" : "com.oracle.truffle.js.runtime",
      "javaCompliance" : "1.8",
      "workingSets" : "Truffle,JavaScript",
    },

    "com.oracle.truffle.js.runtime.doubleconv" : {
      "subDir" : "src",
      "sourceDirs" : ["src"],
      "dependencies" : [
      ],
      "findbugs" : "false",
#     checkstyle and findbugs turned off to keep the source aligned
#     with the original nashorn version as much as possible
      "javaCompliance" : "1.8",
      "workingSets" : "Truffle,JavaScript",
    },

    "com.oracle.truffle.regex.nashorn" : {
      "subDir" : "src",
      "sourceDirs" : ["src"],
      "dependencies" : [
      ],
      "findbugs" : "false",
#     checkstyle and findbugs turned off to keep the source aligned
#     with the original nashorn version as much as possible
      "javaCompliance" : "1.8",
      "workingSets" : "Truffle,Regex",
    },

    "com.oracle.truffle.regex" : {
      "subDir" : "src",
      "sourceDirs" : ["src"],
      "dependencies" : [
        "truffle:TRUFFLE_API",
        "sdk:GRAAL_SDK",
        "com.oracle.truffle.regex.nashorn",
      ],
      "annotationProcessors" : ["truffle:TRUFFLE_DSL_PROCESSOR"],
      "checkstyle" : "com.oracle.truffle.js.runtime",
      "javaCompliance" : "1.8",
      "workingSets" : "Truffle,Regex",
    },

    "com.oracle.truffle.js.stats" : {
      "subDir" : "src",
      "sourceDirs" : ["src"],
      "dependencies" : [
        "com.oracle.truffle.js.shell",
        "NETBEANS_PROFILER",
        "graaljs",
      ],
      "checkstyle" : "com.oracle.truffle.js.runtime",
      "javaCompliance" : "1.8",
      "workingSets" : "Truffle,JavaScript",
    },

    "com.oracle.truffle.js.scriptengine" : {
      "subDir" : "src",
      "sourceDirs" : ["src"],
      "dependencies" : [
        "sdk:GRAAL_SDK",
      ],
      "checkstyle" : "com.oracle.truffle.js.runtime",
      "javaCompliance" : "1.8",
      "workingSets" : "Truffle,JavaScript",
    },

    "com.oracle.truffle.js.scriptengine.test" : {
      "subDir" : "src",
      "sourceDirs" : ["src"],
      "dependencies" : [
        "com.oracle.truffle.js.scriptengine",
        "sdk:GRAAL_SDK",
        "mx:JUNIT",
        "GRAALJS",
      ],
      "checkstyle" : "com.oracle.truffle.js.runtime",
      "javaCompliance" : "1.8",
      "workingSets" : "Truffle,JavaScript",
    },

    "com.oracle.truffle.js.test.external" : {
      "subDir" : "src",
      "sourceDirs" : ["src"],
      "dependencies" : [
        "graal-js:GRAALJS",
        "mx:JUNIT",
        "JACKSON_CORE",
        "JACKSON_ANNOTATIONS",
        "JACKSON_DATABIND",
        "NASHORN_INTERNAL_TESTS",
      ],
      "checkstyle" : "com.oracle.truffle.js.runtime",
      "javaCompliance" : "1.8",
      "workingSets" : "Truffle,JavaScript,Test",
      "testProject" : True,
    },

    "graaljs" : {
      "dependencies" : [
        "com.oracle.truffle.js.parser",
      ],
      "buildDependencies" : ["com.oracle.truffle.js.snapshot"],
      "class" : "GraalJsProject",
      "prefix" : "",
      "outputDir" : "mxbuild/graal/graaljs"
    },

    "icu4j-data": {
        "native": True,
        "class": "Icu4jDataProject",
        "outputDir": "lib/icu4j",
        "prefix": "icu4j"
    },
  },

  "distributions" : {
    "GRAALJS" : {
      "subDir" : "src",
      "dependencies" : ["graaljs"],
      "distDependencies" : [
        "TREGEX",
        "truffle:TRUFFLE_API",
        "sdk:GRAAL_SDK",
      ],
      "exclude": [
        "mx:ASM_DEBUG_ALL",
        "ICU4J",
      ],
      "description" : "Graal JavaScript engine",
      "maven" : {
        "artifactId" : "graal-js",
      },
    },

    "GRAALJS_LAUNCHER" : {
      "subDir" : "src",
      "dependencies" : ["com.oracle.truffle.js.shell"],
      "mainClass" : "com.oracle.truffle.js.shell.JSLauncher",
      "distDependencies" : ["sdk:LAUNCHER_COMMON"],
      "description" : "Graal JavaScript Launcher",
    },

    "TRUFFLE_JS_FACTORY_PROCESSOR" : {
      "subDir" : "src",
      "dependencies" : ["com.oracle.truffle.js.factory.processor"],
      "distDependencies" : [
        "truffle:TRUFFLE_API",
        "sdk:GRAAL_SDK"
      ],
      "maven" : False,
      "overlaps" : ["GRAALJS"],
    },

    "TRUFFLE_JS_SNAPSHOT_TOOL" : {
      "subDir" : "src",
      "dependencies" : ["com.oracle.truffle.js.snapshot"],
      "mainClass" : "com.oracle.truffle.js.snapshot.SnapshotTool",
      "distDependencies" : [
        "GRAALJS",
      ],
      "maven" : False,
    },

    "TREGEX" : {
      "subDir" : "src",
      "dependencies" : ["com.oracle.truffle.regex"],
      "distDependencies" : [
        "truffle:TRUFFLE_API",
        "sdk:GRAAL_SDK"
      ],
    },

    "TRUFFLE_STATS" : {
      "subDir" : "src",
      "mainClass" : "com.oracle.truffle.js.stats.heap.HeapDumpAnalyzer",
      "dependencies" : ["com.oracle.truffle.js.stats"],
      "distDependencies" : [
        "GRAALJS",
        "NETBEANS_PROFILER",
        "GRAALJS_LAUNCHER"
      ],
      "maven" : False,
    },

    "GRAALJS_SCRIPTENGINE" : {
      "subDir" : "src",
      "dependencies" : ["com.oracle.truffle.js.scriptengine"],
      "distDependencies" : [
        "sdk:GRAAL_SDK"
      ],
      "maven" : False,
    },

    "GRAALJS_SCRIPTENGINE_TESTS" : {
      "subDir" : "src",
      "dependencies" : ["com.oracle.truffle.js.scriptengine.test"],
      "distDependencies" : [
        "mx:JUNIT",
        "sdk:GRAAL_SDK",
        "GRAALJS",
        "GRAALJS_SCRIPTENGINE",
      ],
      "maven" : False,
    },

    "TRUFFLE_JS_TESTS" : {
      "dependencies" : ["com.oracle.truffle.js.test.external"],
      "exclude" : [
        "mx:HAMCREST",
        "mx:JUNIT",
        "JACKSON_CORE",
        "JACKSON_ANNOTATIONS",
        "JACKSON_DATABIND",
        "NASHORN_INTERNAL_TESTS",
      ],
      "distDependencies" : ["GRAALJS"],
      "maven" : False,
    },

    "ICU4J-DIST" : {
      "native" : True,
      "relpath" : True,
      "platformDependent" : False,
      "dependencies" : [
        "icu4j-data",
      ],
      "description" : "ICU4J localization library and data files",
    },
  }
}
