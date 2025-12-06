
class MyRunnable implements Runnable {

    private volatile boolean running = true;

    @Override
    public void run() {
        synchronized (this) {
            while (running) {
                System.out.println("Thread ID: " + Thread.currentThread().getId() + " is running.");
                try {
                    this.wait(500);
                } catch (InterruptedException e) {
                    System.out.println("Thread ID: " + Thread.currentThread().getId() + " was interrupted.");
                    // restore interrupted status and stop the loop
                    Thread.currentThread().interrupt();
                    break;
                }
            }
        }
    }

    public void stopThread() {
        running = false;
        synchronized (this) {
            // wake the thread if it's waiting
            this.notifyAll();
        }
    }
}

public class RunnableThreadExample {

    public static void main(String[] args) {
        // Create five instances of MyRunnable 
        MyRunnable myRunnable1 = new MyRunnable();
        MyRunnable myRunnable2 = new MyRunnable();
        MyRunnable myRunnable3 = new MyRunnable();
        MyRunnable myRunnable4 = new MyRunnable();
        MyRunnable myRunnable5 = new MyRunnable();
        // Create five threads and associate them with MyRunnable instances 
        Thread thread1 = new Thread(myRunnable1);
        Thread thread2 = new Thread(myRunnable2);
        Thread thread3 = new Thread(myRunnable3);
        Thread thread4 = new Thread(myRunnable4);
        Thread thread5 = new Thread(myRunnable5);

        // Start the threads 
        thread1.start();
        thread2.start();
        thread3.start();
        thread4.start();
        thread5.start();

        // Sleep for a while to allow the threads to run 
        try {
            Thread.sleep(500);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }

        // Stop the threads gracefully 
        myRunnable1.stopThread();
        myRunnable2.stopThread();
        myRunnable3.stopThread();
        myRunnable4.stopThread();
        myRunnable5.stopThread();
    }
}
