class Nodo:
    def __init__(self, estado, padre, accion):
        self.estado = estado
        self.padre = padre
        self.accion = accion

class Frontera:
    def __init__(self):
        self.frontera =[]
    
    def empty(self):
        return (len(self.frontera) == 0)

    def add(self, nodo):
        self.frontera.append(nodo)
    
    def eliminar(self):
        pass

    def contiene_estado(self, estado):
        return any(nodo.estado == estado for nodo in self.frontera)

class Cola(Frontera):
    def eliminar(self):
        # Termina la busqueda si la frontera esta vacia
        if self.empty():        
            raise Exception("Frontera vacia")
        else:
            # Guardamos el primer item en la lista 
            # (el cual es el nodo añadido de primero)
            nodo = self.frontera[0]
            # Guardamos todos los items excepto el 
            # primero (eliminamos)
            self.frontera = self.frontera[1:]
            return nodo


class SimpleProblemSolvingAgentProgram:
    def __init__(self, initial_state=None, posrobot=None):
        self.state = initial_state
        self.pos = posrobot
    
    def __call__(self, percept):
        self.state = self.update_state(self.state, percept)
        goal = self.formulate_goal(self.state)
        problem = self.formulate_problem(self.state, goal)
        seq = self.search(problem)
        if not seq:
            return None
        return seq
    
    def update_state(self, state, percept):
        return state
    
    def formulate_goal(self, state):
        goal = ((0, 0), ([(0, 0), 'Clean'], [(1, 0), 'Clean']))
        return goal
    
    def formulate_problem(self, state, goal):
        problem = (self.pos, state)
        return problem
    
    def search(self, problem):
        visitado = []
        pos, state = problem
        #print((pos,state))
        goal = self.formulate_goal(state)
        #if state == ([(0, 0), 'Clean'], [(1, 0), 'Clean']):
            #return []
        frontera = Cola()
        inicial = Nodo(problem, None, None)

        frontera.add(inicial)
        visitado.append(inicial)
        while not frontera.empty():
            nodo = frontera.eliminar()
            pos, estado = nodo.estado
            #print(nodo.estado)
            if nodo.estado == goal:
                acciones = []
                #for i in visitado:
                    #print(i.accion)
                visitado.pop(0)
                #print(visitado[0].accion)
                for i in visitado:
                    acciones.append(i.accion)
                

                    
                #acciones.reverse()
                return acciones
            acciones = ["Clean","Right","Left"]
            for accion in acciones:
                rooma = [i for i, room in enumerate(estado) if room[0] == pos][0]
                if accion == "Right" and pos[0] == 1:
                    continue
                elif accion == "Left" and pos[0] == 0:
                    continue
                elif accion == "Clean" and estado[rooma][1] == "Clean":
                    continue
                    
                    
                    
                #print("nodo: ", nodo.estado)
                nuevo_estado = self.result(estado, pos, accion)
                
                #print("accion: ", accion)
                #print("nuevo estado: ", nuevo_estado)
                nuevo_nodo = Nodo(nuevo_estado, nodo, accion)
                if not frontera.contiene_estado(nuevo_estado):
                    frontera.add(nuevo_nodo)
                    visitado.append(nuevo_nodo)
        return None
    
    def result(self, state, pos, action):
        new_state = state  # cambiar a lista
        new_pos = pos
        if action == "Clean":
            room_idx = [i for i, room in enumerate(state) if room[0] == new_pos][0]
            if new_state[room_idx][1] == "Dirty":
                new_state[room_idx][1] = "Clean"
        elif action == "Right":
            if pos[0] < 1:
                new_pos = (pos[0] + 1, pos[1])
        elif action == "Left":
            if pos[0] > 0:
                new_pos = (pos[0] - 1, pos[1])
        return (new_pos, new_state)
        
# Establecer el estado inicial
initial_state = [(0, 0), "Dirty"], [(1, 0), "Dirty"]
pos_robot = (0,0)
# Crear una instancia de SimpleProblemSolvingAgentProgram
agent = SimpleProblemSolvingAgentProgram(initial_state,pos_robot)

# Llamar a la función con el estado inicial como percept
action = agent(initial_state)
print("Acción recomendada:", action)