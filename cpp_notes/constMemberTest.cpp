#include <cstdio>
#include <string>

/*  const member function in C++ :
    1. In C++, member function and constant member function can be overloaded as
        the following example.

    2. It is because C++ internally just add "const" qualifier on "this" parameter
        (,which inplicitly added by compiler) for member function.
         => It is just "overloading with different parameters"...

    3. Therefore, const object cannot use non-const member function
        : Since "const" to "non-const" cast is not allowed.
    4. Non-const object can use const member function.
        : Since "non-const" to "const" cast is allowed.
   */

class TextBlock {
    public:
        TextBlock()                   {};
        TextBlock(std::string s) : text(s) {};
        
        const char& operator[] (std::size_t position) const {
            printf("Const op[] is called\n");
            return text[position];
        }

        char& operator[] (std::size_t position) {
            printf("Non-Const op[] is called, before :");
            return const_cast<char&>(
                   static_cast<const TextBlock&>(*this) [position]
            );
        }

        void print () const {
            fprintf(stdout, "I'm am the %s atomic!\n", text.c_str());
        }

        void nonconst_print () {
            fprintf(stdout, "I'm am the %s atomic!\n", text.c_str());
        }

    private:
        std::string text = "Hello, World";
};

int main(int argc, char* args[]) {

    TextBlock nonConst("NonConst Block");
    nonConst.print();
    char& txt = nonConst[1];
    txt = 'x';
    nonConst.print();
    nonConst.nonconst_print();

    const TextBlock constBlock("Const Block");
    constBlock.print();
    //  constBlock.nonconst_print();    // Compiler forbids this.
    //  char& txt2 = constBlock[1];     // Compiler forbids this.
    const char& txt2 = constBlock[1];

    return 0;
}
