
#include <iostream>

class SomeClass {
public:
	SomeClass() {}
	~SomeClass() {
		std::cout << "Desctructor is invoked" << std::endl;
	}
};

int main(int argc, char **argv) {
	SomeClass some_object;
	std::exit(0); // some_object's desctructor will not be invoked
}
