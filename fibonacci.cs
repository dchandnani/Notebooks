class Test {

    // Hello World
    public void Hello() {
        Console.WriteLine("Hello world!");
    }

    // Fibonacci
    public void Fibonacci(int len)  
    {  
        int a = 0, b = 1, c = 0;  
        Console.Write("{0} {1} ", a,b);  
        for (int i = 2; i < len; i++)  
        {  
            c= a + b;  
            Console.Write("{0} ", c);  
            a= b;  
            b= c;  
        }  
    }
}

Test test = new Test();
test.Hello();
test.Fibonacci(10);
