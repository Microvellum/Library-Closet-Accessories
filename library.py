import os
from mv import fd_types, unit
from . import classes

CLOSET_ACCESSORIES = os.path.join(os.path.dirname(__file__),"Accessories")

#---------PRODUCT: CLOSET ACCESSORIES

class PRODUCT_Broom_Hook(classes.Decorative_Assembly):
    
    def __init__(self):
        self.category_name = "Accessories"
        self.assembly_name = "Broom Hook"
        self.assembly_path = os.path.join(CLOSET_ACCESSORIES,"Broom Hook.blend")
        
class PRODUCT_Closet_Hook_1(classes.Decorative_Assembly):
    
    def __init__(self):
        self.category_name = "Accessories"
        self.assembly_name = "Closet Hook 1"
        self.assembly_path = os.path.join(CLOSET_ACCESSORIES,"Closet Hook 1.blend")
        
class PRODUCT_Closet_Hook_2(classes.Decorative_Assembly):
    
    def __init__(self):
        self.category_name = "Accessories"
        self.assembly_name = "Closet Hook 2"
        self.assembly_path = os.path.join(CLOSET_ACCESSORIES,"Closet Hook 2.blend")
        
class PRODUCT_Closet_Hook_3(classes.Decorative_Assembly):
    
    def __init__(self):
        self.category_name = "Accessories"
        self.assembly_name = "Closet Hook 3"
        self.assembly_path = os.path.join(CLOSET_ACCESSORIES,"Closet Hook 3.blend")
        
class PRODUCT_Closet_Hook_4(classes.Decorative_Assembly):
    
    def __init__(self):
        self.category_name = "Accessories"
        self.assembly_name = "Closet Hook 4"
        self.assembly_path = os.path.join(CLOSET_ACCESSORIES,"Closet Hook 4.blend")
        
class PRODUCT_Coat_and_Hat_Hook(classes.Decorative_Assembly):
    
    def __init__(self):
        self.category_name = "Accessories"
        self.assembly_name = "Coat and Hat Hook"
        self.assembly_path = os.path.join(CLOSET_ACCESSORIES,"Coat and Hat Hook.blend")
        
class PRODUCT_Coat_and_Hat_Hook_2(classes.Decorative_Assembly):
    
    def __init__(self):
        self.category_name = "Accessories"
        self.assembly_name = "Coat and Hat Hook 2"
        self.assembly_path = os.path.join(CLOSET_ACCESSORIES,"Coat and Hat Hook 2.blend")
        
class PRODUCT_Double_Hook(classes.Decorative_Assembly):
    
    def __init__(self):
        self.category_name = "Accessories"
        self.assembly_name = "Double Hook"
        self.assembly_path = os.path.join(CLOSET_ACCESSORIES,"Double Hook.blend")
        
class PRODUCT_Hat_And_Coat_Hook(classes.Decorative_Assembly):
    
    def __init__(self):
        self.category_name = "Accessories"
        self.assembly_name = "Hat And Coat Hook"
        self.assembly_path = os.path.join(CLOSET_ACCESSORIES,"Hat And Coat Hook.blend")
        
class PRODUCT_Ironing_Board(classes.Decorative_Assembly):
    
    def __init__(self):
        self.category_name = "Accessories"
        self.assembly_name = "Ironing Board"
        self.assembly_path = os.path.join(CLOSET_ACCESSORIES,"Ironing Board.blend")
        
class PRODUCT_Jewelry_Tray(classes.Decorative_Assembly):
    
    def __init__(self):
        self.category_name = "Accessories"
        self.assembly_name = "Jewelry Tray"
        self.assembly_path = os.path.join(CLOSET_ACCESSORIES,"Jewelry Tray.blend")
        
class PRODUCT_Mirror(classes.Decorative_Assembly):
    
    def __init__(self):
        self.category_name = "Accessories"
        self.assembly_name = "Mirror"
        self.assembly_path = os.path.join(CLOSET_ACCESSORIES,"Mirror.blend")
        
class PRODUCT_Pants_Rack_1(classes.Decorative_Assembly):
    
    def __init__(self):
        self.category_name = "Accessories"
        self.assembly_name = "Pants Rack 1"
        self.assembly_path = os.path.join(CLOSET_ACCESSORIES,"Pants Rack 1.blend")
        
class PRODUCT_Pants_Rack_2(classes.Decorative_Assembly):
    
    def __init__(self):
        self.category_name = "Accessories"
        self.assembly_name = "Pants Rack 2"
        self.width = unit.inch(18)
        self.assembly_path = os.path.join(CLOSET_ACCESSORIES,"Pants Rack 2.blend")
        
class PRODUCT_Pull_Out_Hamper(classes.Decorative_Assembly):
    
    def __init__(self):
        self.category_name = "Accessories"
        self.assembly_name = "Pull Out Hamper"
        self.width = unit.inch(18)
        self.assembly_path = os.path.join(CLOSET_ACCESSORIES,"Pull Out Hamper.blend")
        
class PRODUCT_Pull_Out_Ironing_Board_Folded(classes.Decorative_Assembly):
    
    def __init__(self):
        self.category_name = "Accessories"
        self.assembly_name = "Pull Out Ironing Board (Folded)"
        self.assembly_path = os.path.join(CLOSET_ACCESSORIES,"Pull Out Ironing Board (Folded).blend")
        
class PRODUCT_Pull_Out_Ironing_Board_Unfolded(classes.Decorative_Assembly):
    
    def __init__(self):
        self.category_name = "Accessories"
        self.assembly_name = "Pull Out Ironing Board (Unfolded)"
        self.assembly_path = os.path.join(CLOSET_ACCESSORIES,"Pull Out Ironing Board (Unfolded).blend")
        
class PRODUCT_Scarf_Rack(classes.Decorative_Assembly):
    
    def __init__(self):
        self.category_name = "Accessories"
        self.assembly_name = "Scarf Rack"
        self.assembly_path = os.path.join(CLOSET_ACCESSORIES,"Scarf Rack.blend")
        
class PRODUCT_Shoe_Fence(classes.Decorative_Assembly):
    
    def __init__(self):
        self.category_name = "Accessories"
        self.assembly_name = "Shoe Fence"
        self.width = unit.inch(18)
        self.assembly_path = os.path.join(CLOSET_ACCESSORIES,"Shoe Fence.blend")
                                                                                                                                                                                  
class PRODUCT_Sliding_Belt_Rack(classes.Decorative_Assembly):
    
    def __init__(self):
        self.category_name = "Accessories"
        self.assembly_name = "Sliding Belt Rack"
        self.assembly_path = os.path.join(CLOSET_ACCESSORIES,"Sliding Belt Rack.blend")
                                                                                                                                                                                                                                                                                  
class PRODUCT_Sliding_Pants_Rack(classes.Decorative_Assembly):
    
    def __init__(self):
        self.category_name = "Accessories"
        self.assembly_name = "Sliding Pants Rack"
        self.width = unit.inch(18)
        self.assembly_path = os.path.join(CLOSET_ACCESSORIES,"Sliding Pants Rack.blend")
                                                                                                                                                                                                                                                                       
class PRODUCT_Sliding_Tie_Rack(classes.Decorative_Assembly):
    
    def __init__(self):
        self.category_name = "Accessories"
        self.assembly_name = "Sliding Tie Rack"
        self.assembly_path = os.path.join(CLOSET_ACCESSORIES,"Sliding Tie Rack.blend")
                                                                                                                                                                                                                                                                       
class PRODUCT_Storage_Box(classes.Decorative_Assembly):
    
    def __init__(self):
        self.category_name = "Accessories"
        self.assembly_name = "Storage Box"
        self.assembly_path = os.path.join(CLOSET_ACCESSORIES,"Storage Box.blend")
                                                                                                                                                                                                                                                                       
class PRODUCT_Tie_And_Belt_Rack(classes.Decorative_Assembly):
    
    def __init__(self):
        self.category_name = "Accessories"
        self.assembly_name = "Tie And Belt Rack"
        self.assembly_path = os.path.join(CLOSET_ACCESSORIES,"Tie And Belt Rack.blend")
                                                                                                                                                                                                                                                                                                                                                 
class PRODUCT_Tie_Hook(classes.Decorative_Assembly):
    
    def __init__(self):
        self.category_name = "Accessories"
        self.assembly_name = "Tie Hook"
        self.assembly_path = os.path.join(CLOSET_ACCESSORIES,"Tie Hook.blend")
                                                                                                                                                                                                                                                     
class PRODUCT_Tilt_Out_Hamper(classes.Decorative_Assembly):
    
    def __init__(self):
        self.category_name = "Accessories"
        self.assembly_name = "Tilt Out Hamper"
        self.assembly_path = os.path.join(CLOSET_ACCESSORIES,"Tilt Out Hamper.blend")
                                                                                                                                                                                                                                                                 
class PRODUCT_Valet_Hanger(classes.Decorative_Assembly):
    
    def __init__(self):
        self.category_name = "Accessories"
        self.assembly_name = "Valet Hanger"
        self.assembly_path = os.path.join(CLOSET_ACCESSORIES,"Valet Hanger.blend")
                                                                                                                                                                                                                                               
class PRODUCT_Valet_rod(classes.Decorative_Assembly):
    
    def __init__(self):
        self.category_name = "Accessories"
        self.assembly_name = "Valet rod"
        self.assembly_path = os.path.join(CLOSET_ACCESSORIES,"Valet rod.blend")
                                                                                                                                                                                                                                                                     
class PRODUCT_Wall_Hooks_1(classes.Decorative_Assembly):
    
    def __init__(self):
        self.category_name = "Accessories"
        self.assembly_name = "Wall Hooks 1"
        self.assembly_path = os.path.join(CLOSET_ACCESSORIES,"Wall Hooks 1.blend")
                                                                                                                                                                                                                                                                       
class PRODUCT_Wall_Hooks_2(classes.Decorative_Assembly):
    
    def __init__(self):
        self.category_name = "Accessories"
        self.assembly_name = "Wall Hooks 2"
        self.assembly_path = os.path.join(CLOSET_ACCESSORIES,"Wall Hooks 2.blend")
                                                                                                                                                                                                                                                      
class PRODUCT_Wardrobe_Lift(classes.Decorative_Assembly):
    
    def __init__(self):
        self.category_name = "Accessories"
        self.assembly_name = "Wardrobe Lift"
        self.assembly_path = os.path.join(CLOSET_ACCESSORIES,"Wardrobe Lift.blend")
                                                                                                                                                                                                                                                                      
                                                                                                                                                                                                                   
                                                                                                                                                                                                                                        
                                                                                                                                                                                                      
                                                                                                                                                                                                                                        
                                                                                                       
                                                                                                                                                                                                               
                                                                                                       
                                                                                                                                                                                                              
                                                                                                                                                                                                                                   
                                                                                                       
                                                                                                                                                                                                              
                                                                                                       
                                                                                                                                                                     
                                                                                                                                                                                                                      
                                                                                                       
                                                                                                                                                                     
                                                                                                       
                                                                                                                                                                                                                                         
                                                                                                       
                                                                                                                                                                     
                                                                                                       
                                                                                                                                                                         
                                                                                                       
                                                                                                                                    
                                                                   
                                                              
                                                                                            
                                                                             
                                                                          
                                                                                            
                                                                             
                                                                                            
                                                              
                                                                                            
                                                                
                                                                
                                                                
                                
                                                               
                                                                                                                                                                              
                                                                 
                                                                    
                                                                       
                                                                 
                                                                    
                                                                           
                                                                  
                                                                           
                                                                        
                                                                      
                                                                        
                                                                   
                                                                                       
                                                                        
                                                                      
                                                                        
                                                                   
                                                                                
                                                
                                                                
                                                                                
                                                
                                
                
                                                                                              
                                                
                                
                
                                                                                           
                                                
                                
                
                                                                                                                             
                                                                                                                                     
                                                                                                              
                                                                                                                                     
                                                                                                                           
                                                                                                                                        
                                                                                                        
                                                                                                        
                                                                                                        
                                                                        
                                        
                                
                                                                                                        
                                                                        
                                        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
                        