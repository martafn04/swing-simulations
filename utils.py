# Classi

class Queue:
    '''Classe coda, per gli elementi da inviare lungo il grafo'''
    def __init__(self):
        self.queue = list()

    def __str__(self):
        return self.queue.__str__()
    
    def __repr__(self):
        return self.__str__()
    
    def __len__(self):
        return len(self.queue)

    def enqueue(self, target):
        '''Inserisco un singolo elemento in fondo alla coda'''
        self.queue.append((target))

    def ensqueue(self, els):
        '''Inserisco più elementi in fondo alla coda (in ordine di apparizione)'''
        for target in els:
            self.enqueue(target)

    def dequeue(self):
        '''Estraggo e ritorno il primo elemento della coda'''
        return self.queue.pop(0)
            
    def is_empty(self):
        return len(self) == 0
    
class Graph:
    '''Classe grafo, con archi diretti in entrambe le direzioni'''
    def __init__(self):
        self.nodes = list()
        self.neighbor = dict()
        self.queue = dict()
        self.n = int()
        self.edges = list()
        self.m = int()

    def __str__(self):
        return self.neighbor.__str__()
    
    def __repr__(self):
        return self.__str__()

    def add_node(self, node):
        if node in self.nodes: pass
        else:
            self.nodes.append(node)
            self.neighbor[node] = set()
            self.n += 1

    def add_nodes(self, nodes):
        for node in nodes:
            self.add_node(node)
    
    def add_edge(self, edge):
        u,v = edge
        if (u,v) not in self.edges and (v,u) not in self.edges:
            self.queue[(u,v)] = Queue()
            self.queue[(v,u)] = Queue()
            if u not in self.nodes:
                self.add_node(u)
                self.n += 1
            if v not in self.nodes:
                self.add_node(v)
                self.n += 1
            self.neighbor[u].add(v)
            self.neighbor[v].add(u)
            self.edges.append((u,v))
            self.m += 1

    def add_edges(self, edges):
        for edge in edges:
            self.add_edge(edge)

    def empty_queues(self):
        '''Ritorno True se tutte le code associate ad ogni arco sono vuote'''
        return True if self.longest_queue() == 0 else False
    
    def longest_queue(self):
        '''Ritorno la lunghezza della coda più lunga'''
        max = 0
        for key in self.queue.keys():
            if len(self.queue[key]) > max:
                max = len(self.queue[key])
        return max
    
    def shortest_queue(self):
        '''Ritorno la lunghezza della coda più corta'''
        min = float('inf')
        for key in self.queue.keys():
            if len(self.queue[key]) < min:
                min = len(self.queue[key])
        return min
    
# Funzioni

def distance(s):
    '''
    Calcola la distanza a cui comunicare allo step s (secondo l'algoritmo Swing)
    
    Args:
        s: step

    Returns:
        int: distanza allo step s
    '''
    return int((1 - (-2)**(s+1)) / 3)

def target(u,s,n):
    '''
    Il target del nodo u allo step s, su un toro di n nodi
    
    Args:
        u: nodo di partenza
        s: step dell'algoritmo
        n: dimensioni del toro

    Returns:
        int: nodo di arrivo
    '''
    return (u + (-1)**u * distance(s)) % n

def supertorus(n, k):
    '''
    Creo il toro con i k link per nodo (che garantiscono comunicazioni private fino allo step k-1) formato da n nodi.
    Un toro 1D base viene fatto chiamando la funzione con k=2.
    
    Args:
        n: dimensioni del toro
        k: numero di step garantiti
    
    Returns:
        Graph: supertoro di dimensioni n, con k link per nodo
    '''
    G = Graph()
    G.add_nodes([i for i in range(n)])
    for s in range(k):
        d = distance(s)
        for node in range(n):
            if node % 2 == 0:
                target = (node + d) % n
                G.add_edge((node, target))
    return G

def honeycomb(b,h):
    '''
    Creo la rete ad alveare, di dimensioni bxh
    
    Args:
        b: base del rettangolo in cui è iscritto il toro
        h: altezza del rettangolo in cui è iscritto il toro

    Returns:
        Graph: toro Honeycomb di dimensioni bxh
    '''
    G = Graph()
    G.add_nodes([(i,j) for i in range(b) for j in range(h)])
    for i in range(b):
        for j in range(h):
            G.add_edges([((i,j),((i+1)%b,j)),((i,j),((i-1)%b,j))])
            if (i%2 == 0 and j%2 == 0) or (i%2 == 1 and j%2 == 1):
                G.add_edge(((i,j),(i,(j+1)%h)))
            else:
                G.add_edge(((i,j),(i,(j-1)%h)))
    return G

def recTorus(b,h):
    '''
    Creo un toro su tassellazione quadrata, con dimensioni bxh


    Args:
        b: base del rettangolo in cui è iscritto il toro
        h: altezza del rettangolo in cui è iscritto il toro

    Returns:
        Graph: toro Honeycomb di dimensioni bxh
    '''
    G = Graph()
    G.add_nodes([(i,j) for i in range(b) for j in range(h)])
    for x in range(b):
        for y in range(h):
            G.add_edge(((x,y),((x+1)%b,y)))
            G.add_edge(((x,y),((x-1)%b,y)))
            G.add_edge(((x,y),(x,(y+1)%h)))
            G.add_edge(((x,y),(x,(y-1)%h)))
    return G