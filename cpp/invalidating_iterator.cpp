#include <vector>
#include <iostream>


int main() {
	
	std::vector<int> v = {1, 2, 3, 4};
	for (auto &i: v) {
			std::cout << i << std::endl;
			v.push_back(i++); // It is invalidating the `v`
	}
	return 0;
}
