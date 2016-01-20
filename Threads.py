import threading
import time

class StoppableThread(threading.Thread):
    """Thread class with a stop() method. The thread itself has to check
    regularly for the stopped() condition."""

    def __init__(self):
        print( "base init")
        super(StoppableThread, self).__init__()
        self._stopper = threading.Event()

    def stopit(self):
        print( "base stop()" )
        self._stopper.set()

    def stopped(self):
        return self._stopper.is_set()


class datalogger(StoppableThread):

    import time

    def __init__(self):
      """
      """
      StoppableThread.__init__(self)
      print( "thread init")

    def run(self):
      print( "thread running" )
      while not self.stopped():
        print( "xx")
        time.sleep(0.13)
      print( "thread ending" )

if __name__ == '__main__':
    test = datalogger()
    test.start()
    time.sleep(3)
    test.stopit()
    test.join()
