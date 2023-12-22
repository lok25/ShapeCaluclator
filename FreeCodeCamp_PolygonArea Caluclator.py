

class Rectangle:

    height=0
    width=0

    def __init__(self, wid, hei):
        self.height=hei
        self.width=wid

    def set_width(self,wid):
        self.width=wid

    def set_height(self,hei):
        self.height=hei

    def get_area(self):
        return self.height* self.width
    
    def get_perimeter(self):
        return 2*(self.height+self.width)
    
    def get_diagnal(self):
        return  (((self.height ** 2 + self.width ** 2) ** .5))
    
    def get_picture(self):
        if(self.width>50):
            return 'Too big for picture.'
        else:
            i=self.height
            j=self.width
            s=""
            while(True):
           
                if(i>0):
                     while(True):

                        if(j>0):
                            s=s+"*"
                            j=j-1
                        
                        else:
                             print(s)
                             s=""
                             j=self.width
                             print('\n')
                             i=i-1 
                             break
                                        

                else:
                     break
                
           

   

            
        
    def get_amount_inside(self, rect):

        return int((self.height*self.width)/(rect.height* rect.width))
    


class Square(Rectangle):
    def set_side (self,side):
        self.width=side
        self.height=side




rect = Rectangle(10, 5)
print(rect.get_amount_inside( rect))
print (rect.get_picture())
print(rect.get_area())
rect.set_height(3)
print(rect.get_perimeter())



        



        

    


