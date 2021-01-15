from DiGraph import DiGraph
from GraphInterface import GraphInterface
from GraphAlgoInterface import GraphAlgoInterface
import sys
import json
import matplotlib.pyplot as plt

class GraphAlgo(GraphAlgoInterface):
    def __init__(self,GRaph=DiGraph()):
        self.gr=GRaph

    def get_graph(self) -> GraphInterface:
        """
        :return: the directed graph on which the algorithm works on.
        """
        return self.gr

    def load_from_json(self, file_name: str) -> bool:
        """
        Loads a graph from a json file.
        @param file_name: The path to the json file
        @returns True if the loading was successful, False o.w.
        """
        self.gr = DiGraph()
        try:
            with open(file_name, 'r') as file:
                jGraph = json.load(file)
                #Insert ALl Nodes Into The Graph
                Nodes = jGraph.get("Nodes")
                for node in Nodes:
                    #Check If There Is Pos Also
                    if len(node) > 1:
                        self.gr.add_node(node_id=node["id"], pos=node["pos"])
                    else:
                        self.gr.add_node(node["id"])
                #Insert ALl Edges Into The Graph
                Edges = jGraph.get("Edges")
                for edge in Edges:
                    self.gr.add_edge(id1=edge["src"], id2=edge["dest"], weight=edge["w"])
            return True

        except IOError as e:
            print(e)
            return False

    def save_to_json(self, file_name: str) -> bool:
        """
        Saves the graph in JSON format to a file
        @param file_name: The path to the out file
        @return: True if the save was successful, False o.w.
        """
        try:
            with open(file_name, 'w') as file:
                Nodes = []
                Edges = []
                for k, v in self.gr.get_all_v().items():
                    # Check If There Is Pos Also
                    if v.pos is not None:
                        print(v.pos)
                        Nodes.append({"id": k, "pos": v.pos})
                    else:
                        Nodes.append({"id": k})
                    dest = self.gr.all_out_edges_of_node(k)
                    if len(dest) > 0:
                        for d, w in dest.items():
                            Edges.append({
                                "src": k,
                                "w": w,
                                "dest": d
                            })
                save = {"Nodes": Nodes,"Edges": Edges}
                json.dump(save, default=self.encoder, indent=4, fp=file)

            return True

        except IOError as e:
            print(e)
            return False

        raise NotImplementedError

    def shortest_path(self, id1: int, id2: int) -> (float, list):
        """
        Returns the shortest path from node id1 to node id2 using Dijkstra's Algorithm
        @param id1: The start node id
        @param id2: The end node id
        @return: The distance of the path, a list of the nodes ids that the path goes through
        """
        ls=[]

        #check if these two nodes Even exist
        if self.gr.Nodes.get(id1, -1) == -1 or self.gr.Nodes.get(id2, -1) == -1:
            # ls[float('inf')]=[]
            ls.append(float('inf'))
            ls.append([])
            return (ls)
        alt=0
        lqueue= []
        dist=[]
        prev = []

        # initially all vertices are unvisited
    	# so v[i] for all i is unvisited
    	# and as no path is yet constructed
    	# dist[i] for all i set to infinity
        for i in range(max(self.gr.get_all_v())+1):
            dist.insert(i, sys.maxsize)
            prev.insert(i, -1)

        for key, value in self.gr.get_all_v().items():
            lqueue.append(key)
        #now source is first to be visited and distance from source to itself should be 0
        dist[id1] = 0
        while len(lqueue) != 0:
            index=self.getIndex(dist,lqueue)
            lqueue.remove(index)
            for n , weight in self.gr.all_out_edges_of_node(index).items():
                if n in lqueue:
                    alt=dist[index]+weight
                    if alt < dist[n]:
                        dist[n]=alt
                        prev[n]=index
        dest = id2
        listarray=[]
        list2=[]
        i=0
        if prev[dest] != -1 or id1 == dest:
            while dest != -1:
                listarray.insert(i, dest)
                i+=1
                dest=prev[dest]
        if i==1 or dist[id2]==sys.maxsize:
            ls.append(float('inf'))
            ls.append([])
            return ls
            # ls[float('inf')]=[]
        else:
            i-=1
            while i>=0:
                list2.append(listarray[i])
                i-=1
            ls.append(dist[id2])
            ls.append(list2)
            # ls[dist[id2]] = list2
        return ls
        raise NotImplementedError

    def connected_component(self, id1: int) -> list:
        """
        Finds the Strongly Connected Component(SCC) that node id1 is a part of.
        @param id1: The node id
        @return: The list of nodes in the SCC
        Notes:
        If the graph is None or id1 is not in the graph, the function should return an empty list []
        """
        #initial queue
        lqueue=[]
        seen=[]
        lqueue.append(id1)
        while len(lqueue) != 0:
            curr=lqueue.pop()
            if not curr in seen:
                #Mark that we have Gone Through It
                self.gr.Nodes[curr].tag=1
                seen.append(curr)
            if self.gr.all_out_edges_of_node(curr):
                for adjacent in self.gr.all_out_edges_of_node(curr):
                    if not adjacent in seen:
                        lqueue.append(adjacent)
        return seen
        raise NotImplementedError

    def connected_components(self) -> [list]:
        """
        Finds all the Strongly Connected Component(SCC) in the graph.
        @return: The list all SCC
        Notes:
        If the graph is None the function should return an empty list []
        """
        #final List that Contains all the connected Nodes
        ls=[]
        #If the graph is None the function should return an empty list []
        if self.gr.v_size() == 0:
            return ls
        #Use Connected_Component Function to iterate over the graph from every element (node)
        for node in self.gr.get_all_v().values():
            if node.tag == 0:
                connected_elements = self.connected_component(node.key)
                # add connected_elements into ls
                ls.append(connected_elements)
        return ls

        raise NotImplementedError

    def plot_graph(self) -> None:
        """
        Plots the graph.
        If the nodes have a position, the nodes will be placed there.
        Otherwise, they will be placed in a random but elegant manner.
        @return: None
        """
        pos_Dict={}
        for k , v in self.gr.get_all_v().items():
            pos = v.pos
            #Check if Pos Is Type Of String if True :-> Split And Cast To Type Tuple
            if isinstance(pos, str):
                pos = pos.split(',')
                pos = tuple(pos)
            # add To Dict of Postions
            pos_Dict[k] = pos
            # print(pos)
            # get Every Node Pos to Draw in the plt
            x = float(pos[0])
            y = float(pos[1])
            plt.plot(x, y, color='red',marker='o', markerfacecolor='white', markersize=20)
            #show the key near each node
            plt.text(x, y, k, fontsize=12, color='black')
        for i in self.gr.get_all_v().keys():
            for j,v in self.gr.all_out_edges_of_node(i).items():
                # print(j,k)
                # print(pos_Dict[j])
            # pos=pos_Dict[k]
                plt.arrow(float(pos_Dict[i][0]),float(pos_Dict[i][1]), float(pos_Dict[j][0])-float(pos_Dict[i][0]),float(pos_Dict[j][1])-float(pos_Dict[i][1]),color='red',linestyle='dashed',linewidth=1,head_width = 0.01,width = 0.05)
                plt.text((float(pos_Dict[i][0])+float(pos_Dict[j][0]))/2 + 0.1, (float(pos_Dict[i][1])+float(pos_Dict[j][1]))/2 + 0.1, v, color='black')
        # setting x and y axis range
        plt.ylim(0, k)
        plt.xlim(0, k)

        # naming the x axis
        plt.xlabel('x',fontsize=12, color='red')
        # naming the y axis
        plt.ylabel('y',fontsize=12, color='red')

        # giving a title to my graph
        plt.title('Graph Plot',fontsize=12, color='red')

        # function to show the plot
        plt.show()

    #func to get the vertex in lQueue with min dist[u]
    def getIndex(self,d: list,q:list) -> int:
        index=0
        min=sys.maxsize
        for i, item in enumerate(d):
            if item<=min and i in q:
                min=item
                index=i
        return index

    def encoder(self,m):
        return m.__dict__
