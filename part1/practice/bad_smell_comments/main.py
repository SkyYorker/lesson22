# В данном коде все прокомментировано как надо,
# но слишком избыточно.
# Избавьтесь от комментариев, изменив имена переменных, 
# чтобы было понятно, за что эти переменные отвечают 
# и что происходит и без комментариев


class Unit:
    # ...
    def mvmntobjbfld(self, field, x_coord: int, y_coord: int, move: bool, fly: bool, crawly: bool, speed: int = 1):
        
        if fly and crawly:
            raise ValueError('Рожденный ползать летать не должен!')

        if fly:  
            speed *= 1.2 
            if move == 'UP':  
                new_y = y_coord + speed   
                new_x = x_coord 
            elif move == 'DOWN':  
                new_y = y_coord - speed   
                new_x = x_coord  
            elif move == 'LEFT':  
                new_y = y_coord  
                new_x = x_coord - speed 
            elif move == 'RIGHT':
                new_y = y_coord 
                new_x = x_coord + speed 
        if crawly:
            speed *= 0.5
            if move == 'UP':
                new_y = y_coord + speed  
                new_x = x_coord  
            elif move == 'DOWN': 
                new_y = y_coord - speed  
                new_x = x_coord 
            elif move == 'LEFT': 
                new_y = y_coord 
                new_x = x_coord - speed 
            elif move == 'RIGHT': 
                new_y = y_coord 
                new_x = x_coord + speed 

            field.set_unit(x=new_x, y=new_y, unit=self)

#     ...
