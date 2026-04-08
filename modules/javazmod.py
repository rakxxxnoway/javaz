import os

import constants

class JavaZ:
    _BUILD_FILE_NAME     = "build"
    _START_FILE_NAME     = "start"
    _RIGHTS              = "770"                        # rwx for user and group

    _ROOT_PATH           = "/usr/local/share/javaz"
    _MAIN_JAVA_PATH      = "src/main/Main.java"

    # CPP LIB
    _CPP_IOSSTREAM       = "iostream"
    _C_STDIO             = "stdio.h"
    _CPP_OWN             = "libbsopen"

    _VERSION             = "1.0.2"

    STDO                = "[\033[92m*\033[0m]: "
    STDE                = "[\033[91m!\033[0m]: "

    LANG_CPP            = "c++"
    LANG_JAVA           = "java"


    def __init__(self, project_name:str) -> None:
        # c++
        self.compiler           = "g++"
        self.compiler_version   = "c++20"
        self.file_extension     = "cpp"
    
        # c
        self.compiler_c         = "gcc"
        self.compiler_c_ver     = "c17"
        self.file_c_ext         = "c"

        # init
        self.project_name = project_name


    #-------------- getters --------------
    @property
    def _java_std_file(self) -> str:
        return constants.JAVA_STD_FILE

    #-------------- cmd generation --------------
    def cmd_mkdir(self, mode:int) -> list:
        """
        Modes\n
        0   - c++\n
        1   - gradle\n
        """

        cmd = constants.CMD_MKDIR_CONTENT.copy()
        if mode == 1:
            cmd.append(self.project_name)

        else:
            cmd.append(self.project_name+"/lib")

        return cmd
    

    def cmd_mkdir_java(self, dir:str) -> list:
        cmd = constants.CMD_MKDIR_CONTENT.copy()

        match dir:
            case "src" | "out":
                cmd.append(f"{self.project_name}/{dir}")
                return cmd
            
            case "main":
                cmd.append(f"{self.project_name}/src/{dir}")
                return cmd
            
        return []

    
    @property
    def cmd_gradle_init(self) -> list:
        cmd = constants.CMD_GRADLE_CONTENT.copy()
        cmd.append(self.project_name)

        return cmd
    
    @property
    def cmd_remove_content(self) -> list:
        cmd = constants.CMD_REMOVER_PROJECT.copy()
        cmd.append(f"{self.project_name}/")

        return cmd
    

    def cmd_chmod(self, file_type:str) -> list:
        cmd = ["chmod", self._RIGHTS]

        if file_type == self._BUILD_FILE_NAME:
            cmd.append(f"{self.project_name}/{self._BUILD_FILE_NAME}")

        else:
            cmd.append(f"{self.project_name}/{self._START_FILE_NAME}")

        return cmd
    
    def cmd_cp_local_lib(self, fext:str) -> list:
        return [ "cp", f"{self._ROOT_PATH}/std/{self._CPP_OWN}.{fext}", f"{self.project_name}/lib/" ]
    

    #-------------- file content generation --------------
    def _gen_build_file(self, build_param: str) -> str:
        return f"""#!/bin/bash
clear

if [ "$#" -eq 0 ]; then
    find src -name '*.java' | xargs javac -d out
    {build_param}

else
    if [ "$1" == "makepkg" ]; then
        mkdir "src/$2"
        echo -e "\033[92mPackage created!\033[0m"
    fi
fi"""

    def _gen_make_file(self, target: str, lang: str) -> str:
        comp = self.compiler
        stdc = self.compiler_version
        fext = self.file_extension

        if lang != self.LANG_CPP:
            comp = self.compiler_c
            stdc = self.compiler_c_ver
            fext = self.file_c_ext

        return f"""CC={comp}
CCFLAGS=-std={stdc} -Wall -g
TARGET={target}
SRCS=main.{fext} $(wildcard lib/*.{fext})
OBJS=$(SRCS:.{fext}=.o)

all: $(TARGET)

$(TARGET): $(OBJS)
\t$(CC) $(CCFLAGS) $(OBJS) -o $(TARGET)

%.o: %.{fext}
\t$(CC) $(CCFLAGS) -c $< -o $@

clean:
\trm -f $(OBJS) $(TARGET)"""
    
    def _gen_c_cpp_file(self, lang:str, author:str, description:str) -> str:
        lib = self._CPP_IOSSTREAM

        if lang != self.LANG_CPP:
            lib = self._C_STDIO

        top_part = f"""/*
 * This {description} written by {author}
 * All rights reserved 2025 - ... ©
*/
#include <{lib}>
"""
        return top_part + constants.C_CPP_BOTTOM
    
    def _gen_start_file(self, lang) -> str:
        open_vim = "./src/main/Main.java"

        if lang == self.LANG_CPP:
            open_vim = "./main.cpp"
        
        add_str = f"nvim {open_vim} -c NERDTree"

        return constants.START_FILE + add_str


    #-------------- file creation methods --------------
    def create_build_file(self, build_params:str) -> None:
        with open(f"{self.project_name}/{self._BUILD_FILE_NAME}", "w") as f:
            f.write(self._gen_build_file(build_params))

    def create_start_file(self, lang="java") -> None:
        with open(f"{self.project_name}/{self._START_FILE_NAME}", "w") as f:
            f.write(self._gen_start_file(lang))

    def create_java_file(self) -> None:
        with open(f"{self.project_name}/{self._MAIN_JAVA_PATH}", "w") as f:
            f.write( self._java_std_file )

    def create_c_file(self, lang:str, author="", description="") -> None:
        with open(f"{self.project_name}/main.{'cpp' if lang == 'c++' else 'c'}", "w") as f:
            f.write(self._gen_c_cpp_file(lang, author, description))

    def create_make_file(self, target:str, lang:str) -> None:
        with open(f"{self.project_name}/Makefile", "w") as f:
            f.write(self._gen_make_file(target, lang))


    #-------------- static --------------
    @staticmethod
    def err(e:Exception) -> Exception:
        print(f"{JavaZ.STDE}{e}")

    @staticmethod
    def version() -> str:
        return f"Java Ez by rNtR\nCurrent version: {JavaZ._VERSION}\n"
    
    @staticmethod
    def dict_to_list(d:dict) -> list:
        return [i for p in d.items() for i in p]
    
    @staticmethod
    def get_program_description() -> str:
        return constants.HELP_DESCRIPTION
    
    @staticmethod
    def get_program_epilog() -> str:
        return constants.EPILOG
    
    @staticmethod
    def gradle_all_types() -> list:
        return constants.GRADLE_ALL
    
    @staticmethod
    def gradle_supported_scriptl() -> list:
        return constants.GRADLE_SCRIPT_LANG
