#include <iostream>
#include <string>


class A {

	std::string m_name;
public:

	
	A(std::string name): m_name(name) {
		
		std::cout << "I'm " << m_name << " " << std::endl;
		std::cout << "In the contructor!" << std::endl;
	}

	A(const A& a): m_name(a.getName()) {

		std::cout << "I'm " << m_name << " " << std::endl;
		std::cout << "In the copy contructor!" << std::endl;
	}

	A(const A&& a): m_name(std::move(a.getName())) {
		std::cout << "I'm " << m_name << " " << std::endl;
		std::cout << "In the move constructor!" << std::endl;
	}

	std::string getName() const {
		return m_name;
	}
};


class B {
	A m_A;
public:
	B(A a): m_A(std::move(a)) {}

};


int
main(int argc, char *argv[]) {

	auto a = A("Hello");
	auto b = a;
	auto c = A{"Bye"};

	A d{"Hi"};
	std::string name = A(A{"Ali"}).getName();

	B x{A("Foo")};

	return 0;
}
