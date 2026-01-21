/*
    ================
    Info: Standard lib for c4kau includes default and most used methods/functions and macros
    Module: libbsopen.hpp
    Written by: RnTr (rax - not the register)
	
	Version: 1.1.1
	Last Modified: 23/08/2025
    ================
*/

#ifndef SYSLIB_HPP
#define SYSLIB_HPP

#include <string>
#include <vector>


// decorations
#define STDO "[*] "s
#define STDI "[+] "s
#define STDE "[!] "s
#define STDIN "[i] "s


/* functions */
void fout(const std::string& ptf);

std::string boolean(bool condition);
std::string boolean(bool condition, bool color);

std::string tlcase(std::string str);
std::string tucase(std::string str);

std::vector<std::string> split(const std::string& text, char delim);


/* ANSI color codes */
enum class Colors : int
{
	BLACK 		= 30,
	DRED 		= 31,
    DGREEN 		= 32,
    DYELLOW 	= 33,
    DBLUE 		= 34,
    DMAGENTA	= 35,
    DCYAN 		= 36,
    DGRAY 		= 90,

    /* bright colors */
    GRAY		= 37,
    RED 		= 91,
    GREEN 		= 92,
    YELLOW 		= 93,
    BLUE 		= 94,
    MAGENTA 	= 95,
    CYAN 		= 96,
    WHITE 		= 97
};


/* classes */
class Colorama
{
private:
    static std::string COLOR;

public:
    static const std::string RESET;

    static std::string fore(Colors color, const std::string& text);
    static std::string back(Colors color, const std::string& text);
    static std::string color(Colors color);
    static std::string bcolor(Colors color);
};

#endif
