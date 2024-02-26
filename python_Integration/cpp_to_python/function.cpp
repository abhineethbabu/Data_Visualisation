extern "C" {
    int my_cpp_function(int a, int b) {
        return a + b;
    }
}


// g++ -shared -o mycppfunction.so -fPIC mycppfunction.cpp
