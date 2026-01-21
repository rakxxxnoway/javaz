CC=g++
CCFLAGS=-std=c++20 -Wall -g
TARGET=run
SRCS=main.cpp $(wildcard lib/*.cpp)
OBJS=$(SRCS:.cpp=.o)

all: $(TARGET)

$(TARGET): $(OBJS)
	$(CC) $(CCFLAGS) $(OBJS) -o $(TARGET)

%.o: %.cpp
	$(CC) $(CCFLAGS) -c $< -o $@

clean:
	rm -f $(OBJS) $(TARGET)