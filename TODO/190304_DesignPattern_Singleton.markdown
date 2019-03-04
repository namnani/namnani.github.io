# 싱글톤이란?
- 싱글턴 패턴(Singleton Pattern)은 인스턴스가 오직 하나만 생성되는 것을 보장하고 어디에서든 이 인스턴스에 접근할 수 있도록 하는 디자인 패턴.

# 싱글톤의 문제점
- 다중 스레드 애플리케이션의 경우에 1개 이상의 인스턴스가 만들어지는 문제가 있다.
- 클래스가 상태를 유지해야 하는 경우에 문제가 된다.

# 해결 방법
1. 정적 변수에 인스턴스를 만들어 바로 초기화하는 방법
ex) private static Printer printer = new Printer();

2. 인스턴스를 만드는 메서드에 동기화하는 방법.
ex) public synchronized static Priner getPrinter(){
 if(printer == null){
  printer = new Printer();
 }
 return printer;
}

ex) public void print(String str){
 synchronized(this){
  counter++;
  System.out.println(str + counter);
 }
}

# etc
- 굳이 싱글턴 패턴을 사용하지 않고 정적 메서드로만 이루어진 정적 클래스(static class)를 사용해도 동일한 효과를 얻을 수 있다.
- 그러나 정적 메서드는 인터페이스에서 사용할 수 없다.
