
abstract class Shape1 {
}

class Circle1 extends Shape1 {

    private final double radius;

    public Circle1(double radius) {
        this.radius = radius;
    }

    double calculateArea() {
        return Math.PI * radius * radius;
    }

    double calculatePerimeter() {
        return 2 * Math.PI * radius;
    }
}

class Triangle1 extends Shape1 {

    private final double side1;
    private final double side2;
    private final double side3;

    public Triangle1(double side1, double side2, double side3) {
        this.side1 = side1;
        this.side2 = side2;
        this.side3 = side3;
    }

    double calculateArea() {
        // Using Heron's formula to calculate the area of a triangle 
        double s = (side1 + side2 + side3) / 2;
        return Math.sqrt(s * (s - side1) * (s - side2) * (s - side3));
    }

    double calculatePerimeter() {
        return side1 + side2 + side3;
    }
}

public class ShapeDemo1 {

    public static void main(String[] args) {
        // Creating Circle and Triangle objects 
        Circle1 circle = new Circle1(5.0);
        Triangle1 triangle = new Triangle1(3.0, 4.0, 5.0);

        // Calculating and displaying area and perimeter 
        System.out.println("Circle Area: " + circle.calculateArea());
        System.out.println("Circle Perimeter: " + circle.calculatePerimeter());

        System.out.println("\nTriangle Area: " + triangle.calculateArea());
        System.out.println("Triangle Perimeter: " + triangle.calculatePerimeter());
    }
}
