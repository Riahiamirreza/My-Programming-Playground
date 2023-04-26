#include <thread>
#include <iostream>



int
main(int argc, char* argv[]) {

	auto count = [&] (int times) {
		for (size_t i = 0; i < times; i++)
			std::cout << i << std::endl;
	};

	std::thread t1 = std::thread(count, 10);
	std::thread t2 = std::thread(count, 15);
	std::thread t3 = std::thread(count, 20);
	std::thread t4 = std::thread(count, 5);


	t1.join();
	t2.join();
	t3.join();
	t4.join();
	return 0;
}


