#include <vector>
#include <iostream>


class A{

        public:

        A() = default;

        A(const A& obj){
                std::cout << "Copy c-tor" << std::endl;
        }

        A(A&& obj){
                std::cout << "Move c-tor" << std::endl;
        }
};



int main(int argc, char *argv[]){

        std::vector<A> vA;

        std::cout << "Copy ctor will be invoked: " << std::endl;
        auto a = A();
        vA.push_back(a);

        std::cout << "Move ctor will be invoked: " << std::endl;
        vA.push_back(A());

        return 0;
}

