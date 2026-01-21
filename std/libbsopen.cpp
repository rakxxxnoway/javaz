/*
    ================
    Info: C++ source library file for c4kau
    Module: libbsopen.cpp
    Written by: RnTr (rax - not the register)
	
	Version: 1.1.1
	Last modified: 23/08/2025
    ================
*/

#include "libbsopen.hpp"

#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>
#include <ctime>
#include <algorithm>
#include <cctype>


using namespace std::literals;



/* static field */
std::string Colorama::COLOR = "\033[";
const std::string Colorama::RESET = "\033[0m";


/* methods */
std::string Colorama::fore(Colors color, const std::string& text)
{
    return COLOR + std::to_string(static_cast<int>(color)) + "m"s + text + RESET;
}


std::string Colorama::back(Colors color, const std::string& text)
{
    return COLOR + std::to_string(static_cast<int>(color) + 10) + "m"s + text + RESET;
}


std::string Colorama::color(Colors color)
{
    return COLOR + std::to_string(static_cast<int>(color)) + "m"s;
}


std::string Colorama::bcolor(Colors color)
{
    return COLOR + std::to_string(static_cast<int>(color) + 10) + "m"s;
}


/* other: */

/* startup banner */
void fout(const std::string& ptf)
{
	std::ifstream file_stream(ptf);

	if(!file_stream.is_open())
	{
		std::cerr << "Couldn't open file: '"s +ptf+ "'\n"s;
		return;
	}

	std::string line;

	while(std::getline(file_stream, line))
		std::cout << line << std::endl;
}


std::string boolean(bool condition)
{
	return (condition) ? "true"s : "false"s;
}


std::string boolean(bool condition, bool color = false)
{
	if(condition)
		return color ? Colorama::color(Colors::GREEN) + "true"s + Colorama::RESET : "true"s;

	return color 	 ? Colorama::color(Colors::RED) + "false"s + Colorama::RESET : "false"s;
}


std::string tlcase(std::string str)
{
	std::transform(str.begin(), str.end(), str.begin(),
			[](unsigned char c){
				return std::tolower(c);
	});

	return str;
}


std::string tucase(std::string str)
{
	std::transform(str.begin(), str.end(), str.begin(),
			[](unsigned char c){
				return std::toupper(c);
	});

	return str;
}

std::vector<std::string> split(const std::string& text, char delim)
{
	std::stringstream tosplit(text);
	std::vector<std::string> splitted;
	std::string block;

	while(std::getline(tosplit, block, delim))
		splitted.push_back(block);

	return splitted;
}
