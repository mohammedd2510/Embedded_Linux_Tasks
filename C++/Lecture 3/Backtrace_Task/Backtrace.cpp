#include "Backtrace.hpp"

void PRINT_BT() {
    boost::stacktrace::stacktrace st;
    std::vector<std::string>Functions_Names;
    std::vector<int>Functions_Lines;
    std::size_t index = 0;
    for (auto& frame: st) 
    {
        if (index == 0) 
        {
            index++;
            continue;
        }
        else
        {
            Functions_Names.insert(Functions_Names.begin(),frame.name()); 
            Functions_Lines.insert(Functions_Lines.begin(),frame.source_line());    
            if (frame.name() == "main") 
            {
                break;
            }
        }
        index++; 
    }
    index = 0;
    for (auto trace: Functions_Names){
        std::cout << index <<" - "<< trace << " -> Line Number "<< Functions_Lines[index]<< std::endl;
        index++;
    }

}