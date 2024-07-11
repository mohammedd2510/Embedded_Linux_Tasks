#ifndef LED_HPP_H
#define LED_HPP_H

class test{

};
class led: public test
{
    private:
        int pin;
        int count;
        bool state;
        int const x;
    public:
        static int number;
        void Print();
        void Display()const;
        /**
         * @brief sayhello
         * 
         * @param temp
         * @return void 
         */
        static void SayHello(int temp);
        led();
        led(int pin,int count , bool state , int x) ;
        /**
         * @brief saybye
         * @param void
         * @param void2
         * @return void
         */
        void saybye(){

        }
        /**
         * @brief doxygentask
         * @param int finished
         * @return void
         */
        void mohamed_osama(){
            
        }

};




#endif