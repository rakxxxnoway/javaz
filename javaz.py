#!/usr/bin/env python3
import subprocess
import argparse
import os

from modules.javazmod import JavaZ


#---------------------------------------------------------------------------------------
# java
def create_simple_project(project_name: str, main: bool = False, empty: bool = False) -> None:
    jz = JavaZ(project_name)

    print(f"{jz.STDO}Creating project '{project_name}'...")

    try:
        subprocess.run( jz.cmd_mkdir_java("src") )
        subprocess.run( jz.cmd_mkdir_java("out") )

        build_param = ""

        if main:
            subprocess.run(jz.cmd_mkdir_java("main"))
            jz.create_java_file()
            build_param = "java -cp out main.Main"

        # creating new build file in root dir
        print(f"{jz.STDO}Creating a new compiling file for project...")
        jz.create_build_file(build_param)

        print(f"{jz.STDO}Creating a new ide starting file for project...")
        jz.create_start_file()

        subprocess.run(jz.cmd_chmod("build"))
        subprocess.run(jz.cmd_chmod("start"))

    except Exception as e:
        JavaZ.err(e)


# gradle
def create_gradle_project(project_name: str, all: bool = False, type: str = None, dsl: str = None, pkg: str = None) -> None:
    jz = JavaZ(project_name)
    print(f"{jz.STDO}Creating project '{project_name}'...")

    try:
        subprocess.run( jz.cmd_mkdir(1) )
        cmd = jz.cmd_gradle_init
        args = {}

        if all:
            args = { "--type": "java-application", "--dsl": "kotlin", "--package": "main" }
        else:
            if type:
                args["--type"] = type
            if dsl:
                args["--dsl"] = dsl
            if pkg:
                args["--package"] = pkg

        parms = JavaZ.dict_to_list(args)
        
        print(f"{jz.STDO}Creating a new ide starting file for project...")
        jz.create_start_file()

        subprocess.run(cmd + parms)

    except Exception as e:
        JavaZ.err(e)


#-----------------------------------------------------------------------------------------------
# cpp
def create_make_project(project_name: str, lang: str, include_local: bool = False, make: str = None) -> None:
    jz = JavaZ(project_name)
    print(f"{jz.STDO}Creating new project '{project_name}...'")

    try:
        subprocess.run( jz.cmd_mkdir(0) )
        jz.create_c_file(lang)

        print(f"{jz.STDO}Creating a new ide starting file for project...")
        jz.create_start_file(jz.LANG_CPP)

        subprocess.run(jz.cmd_chmod("start"))

        if include_local:
            print(f"{jz.STDO}Adding Custom STD library...")
            subprocess.run( jz.cmd_cp_local_lib("cpp") )
            subprocess.run( jz.cmd_cp_local_lib("hpp") )

        if make:
            print(f"{jz.STDO}Creating Makefile...")
            jz.create_make_file(make, lang)

    except Exception as e:
        JavaZ.err(e)


def remove_project(project_name:str) -> None:
    jz = JavaZ(project_name)
    try:
        subprocess.run( jz.cmd_remove_content )

    except Exception as e:
        JavaZ.err(e)

def file_name() -> str:
    return os.path.basename(__file__)


# parser initialization
def init_parse() -> argparse.Namespace:
    """
    javaz create [project_language] [project_name] (flags)\n
    javaz remove project_name
    """

    arg = argparse.ArgumentParser( prog=file_name(), description=JavaZ.get_program_description(), epilog=JavaZ.get_program_epilog() )
    root_subargs = arg.add_subparsers(dest="root", required=True)

    remove = root_subargs.add_parser("remove", help="Remove project")
    remove.add_argument("project_name")

    create  = root_subargs.add_parser("create", help="Creates a new project")
    lang    = create.add_subparsers(dest="language", required=True)

    # java
    java = lang.add_parser("java", help="Java project")
    java.add_argument("project_name", help="Path to where project will be created")

    single = java.add_mutually_exclusive_group()
    single.add_argument(
        "--main", "-m",
        action="store_true",
        help="Specify if you want a pregenerated project with files"
    )
    single.add_argument(
        "--empty", "-e", "--none",
        action="store_true",
        help="Creates an empty project with only required files and directories"
    )

    #gradle
    gradle = lang.add_parser("gradle", help="Gradle project")
    gradle.add_argument("project_name", help="Path to where project will be created")

    gradle.add_argument(
        "--all",
        action="store_true",
        help="Creates a default gradle project"
    )
    gradle.add_argument(
        "--type", "-t",
        choices=JavaZ.gradle_all_types(),
        help="Specify a type of a gradle project"
    )
    gradle.add_argument(
        "--dsl",
        choices=JavaZ.gradle_supported_scriptl(),
        help="Specify script language"
    )
    gradle.add_argument(
        "--pkg", "-p",
        help="Package name"
    )


    #c++
    cpp = lang.add_parser("c++", help="C++ project")
    cpp.add_argument("project_name")
    cpp.add_argument("--make")
    cpp.add_argument("--include-local", action="store_true")

    #c
    #c = lang.add_parser("c", help="C project")

    return arg.parse_args()


# main
def main() -> None:
    args = init_parse()
    pname = args.project_name

    if args.root == "create":
        match args.language:
            case "java":
                create_simple_project( pname, main=args.main, empty=args.empty )

            case "gradle":
                create_gradle_project( pname, all=args.all, type=args.type, dsl=args.dsl, pkg=args.pkg )

            case "c++":
                create_make_project( pname, "c++", include_local=args.include_local, make=args.make)

    elif args.root == "remove":
        remove_project(args.project_name)


#=================== PROGRAM ===================
if __name__ == "__main__":
    main()
