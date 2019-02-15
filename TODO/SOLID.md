# SOLID 원칙

1. Single Responsibility Principle (SRP, 단일 책임 원칙)
- 하나의 클래스는 단 하나의 책임만을 가져야 한다.

2. Open-Closed Principle(OCP, 개방-폐쇄 원칙)
- 기존의 코드는 변경하지 않으면서 기능을 추가할 수 있도록 설계.

3. Liskov Substitution Principle(LSP, 리스코프 치환 원칙)
- 부모클래스의 인스턴스를 자식클래스의 인스턴스로 대신할 수 있어야 한다.
- 피터 코드의 상속 규칙을 지키는 것.
- 상속은 하면서 재정의하지 않는 느낌? 인 것 같다...

4. Dependency Inversion Principle(DIP, 의존 역전 원칙)
- 변화하기 어려운 것, 변화가 없는 것에 의존하다.
- 인터페이스나 추상클래스에 의존하라!
- 의존성 주입으로 변화를 쉽게 수용 가능! (즉, setter() 메소드가 있어야함)

5. Interface Segregation Principle(ISP, 인터페이스 분리 원칙)
- 인터페이스를 클라이언트에 특화되도록 잘게 쪼개라!


*SRP -> ISP
SRP이면 반드시 ISP 인 것은 아니다.