#include <algorithm>
#include <vector>
#include <iostream>
#include <fstream>



void print(std::vector<std::string> answer) {
  size_t j;
  for (j = 0; j < answer.size(); j++) {
    std::cout << answer[j] << std::endl;
  }
}

int main(int argc, char ** argv) {
  
  std::ifstream read;
  std::string strings;
  std::vector<std::string> answer;
  
  if (argc == 1) {
    while (!std::cin.eof()) {
      std::getline(std::cin, strings);
      answer.push_back(strings);
     
      std::sort(answer.begin(), answer.end());
      
      print(answer);
      answer.clear();
    }
  }
  else {
    int i;
    for (i = 1; i < argc; i++) {
      read.open(argv[i]);
      if (read.fail()) {
        std::cerr << "cannot read" << std::endl;
        return EXIT_FAILURE;
      }
      while (!read.eof()) {
        std::getline(read, strings);
        answer.push_back(strings);
      }
   
      std::sort(answer.begin(), answer.end());
    
      print(answer);
      answer.clear();
      read.close();
    }
  }
  return EXIT_SUCCESS;
}
