from abc import ABC,abstractmethod
import numpy as np

class BaseProcessor(ABC):
    """Base processor class."""
    
    def __init__(self) -> None:
        """Inits BaseProcessor."""
        self.__enable:bool = False

    @abstractmethod
    def process(self, image:np.ndarray) -> np.ndarray:
        """Process numpy 2d data(image)

        Args:
        image: numpy 2d data

        Returns:
        numpy 2d data

        """
        return image

    @property
    def enable(self) -> bool:
        """Enable getter

            Returns:
            enable value

        """
        return self.__enable

    @enable.setter
    def enable(self, value:bool)-> None:
        """Enable setter.

        Args:
        value: boolean value

        """
        self.__enable:bool = value

class Lens(BaseProcessor):
    """Lens class."""
    
    def __init__(self, width:int, height:int) -> None:
        """Inits Lens.
        
        Args:
        width: lens width
        height: lens height

        """
        
        super().__init__()
        self.__height = height
        self.__width = width 

    
    def process(self, image:np.ndarray) -> np.ndarray:
        """Process numpy 2d data(image)

        Args:
        image: numpy 2d data

        Returns:
        numpy 2d data

        Raises:
            ValueError: If input image doesn't match Lens size
        """
        if image.shape != (self.__width, self.__height):
            raise ValueError(f'Image width or height mismatch') 

        return image

    @property
    def height(self) -> int:
        """Height getter

            Returns:
            height value

        """
        return self.__height

    @height.setter
    def height(self, value:int)-> None:
        """Height setter.

        Args:
        value: float value

        """
        self.__height = value

    @property
    def width(self) -> int:
        """Height getter

            Returns:
            height value

        """
        return self.__width

    @width.setter
    def width(self, value:int)-> None:
        """Width setter.

        Args:
        value: float value

        """
        self.__width = value        

class Sensor(BaseProcessor):
    """Sensor class."""
    
    def __init__(self, gain:float) -> None:
        """Inits Sensor.
        
        Args:
        gain: sensor gain

        """
        
        super().__init__()  
        self.__gain = gain

    
    def process(self, image:np.ndarray) -> np.ndarray:
        """Process numpy 2d data(image)

        Args:
        image: numpy 2d data

        Returns:
        numpy 2d data

        """
        print('image:',image)

        return np.dot(self.__gain, image)

    @property
    def gain(self) -> float:
        """Gain getter

            Returns:
            gain value

        """
        return self.__gain

    @gain.setter
    def gain(self, value:float)-> None:
        """Gain setter.

        Args:
        value: float value

        """
        self.__gain = value
