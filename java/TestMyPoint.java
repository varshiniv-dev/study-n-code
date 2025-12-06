//Develop the code for the class MyPoint. Also develop a JAVA program (called TestMyPoint) to test all the methods defined in the class. 

class MyPoint {

    private int x;
    private int y;

    // Default constructor 
    public MyPoint() {
        this.x = 0;
        this.y = 0;
    }

    // Overloaded constructor 
    public MyPoint(int x, int y) {
        this.x = x;
        this.y = y;
    }

    // Set both x and y 
    public void setXY(int x, int y) {
        this.x = x;
        this.y = y;
    }

    public int[] getXY() {
        return new int[]{x, y};
    }

    // Return a string description of the instance in the format "(x, y)" 
    @Override
    public String toString() {
        return "(" + x + ", " + y + ")";
    }

    // Calculate distance from this point to another point at (x, y) coordinates 
    public double distance(int x, int y) {
        int xDiff = this.x - x;
        int yDiff = this.y - y;
        return Math.sqrt(xDiff * xDiff + yDiff * yDiff);
    }

    // Calculate distance from this point to another MyPoint instance (another) 
    public double distance(MyPoint another) {
        return distance(another.x, another.y);
    }

    public double distance() {
        return distance(0, 0);
    }

}

public class TestMyPoint {

    public static void main(String[] args) {
        // Creating MyPoint objects using different constructors 
        MyPoint point1 = new MyPoint();
        MyPoint point2 = new MyPoint(3, 4);

        // Testing setXY and getXY methods 
        point1.setXY(1, 2);
        System.out.println("Point1 coordinates after setXY: " + point1.getXY()[0] + ", " + point1.getXY()[1]);

        // Testing toString method 
        System.out.println("Point2 coordinates: " + point2.toString());

        // Testing distance methods 
        System.out.println("Distance from Point1 to Point2: " + point1.distance(point2));
        System.out.println("Distance from Point2 to Origin: " + point2.distance());
    }
}
