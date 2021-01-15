from GraphInterface import GraphInterface
from NodeData import NodeData

class DiGraph(GraphInterface):
    def __init__(self):
        self.edgeSize=0
        self.mc=0
        self.Nodes = {}
        self.Edges = {}
        self.Edges_In={}
    """
    Returns the number of vertices in this graph
    @return: The number of vertices in this graph
    """
    def v_size(self) -> int:
        return len(self.Nodes)
        raise NotImplementedError

    """
    Returns the number of edges in this graph
    @return: The number of edges in this graph
    """
    def e_size(self) -> int:
        return self.edgeSize
        raise NotImplementedError

    """return a dictionary of all the nodes in the Graph, each node is represented using a pair
     (node_id, node_data)
    """
    def get_all_v(self) -> dict:
        return self.Nodes

    """return a dictionary of all the nodes connected to (into) node_id ,
    each node is represented using a pair (other_node_id, weight)
     """
    def all_in_edges_of_node(self, id1: int) -> dict:
        return self.Edges_In[id1]


    def all_out_edges_of_node(self, id1: int) -> dict:
        """return a dictionary of all the nodes connected from node_id , each node is represented using a pair
        (other_node_id, weight)
        """
        return self.Edges[id1]


    def get_mc(self) -> int:
        """
        Returns the current version of this graph,
        on every change in the graph state - the MC should be increased
        @return: The current version of this graph.
        """
        return self.mc
        raise NotImplementedError

    def add_edge(self, id1: int, id2: int, weight: float) -> bool:
        """
        Adds an edge to the graph.
        @param id1: The start node of the edge
        @param id2: The end node of the edge
        @param weight: The weight of the edge
        @return: True if the edge was added successfully, False o.w.
        Note: If the edge already exists or one of the nodes dose not exists the functions will do nothing
        """
        # check if key exists in dictionary by checking if get() returned default value
        if self.Edges[id1].get(id2, -1) == -1:
            self.Edges[id1][id2]=weight
            self.Edges_In[id2][id1]=weight
            self.edgeSize += 1
            self.mc +=1
            return True
        return False
        raise NotImplementedError

    def add_node(self, node_id: int, pos: tuple = None) -> bool:
        """
        Adds a node to the graph.
        @param node_id: The node ID
        @param pos: The position of the node
        @return: True if the node was added successfully, False o.w.
        Note: if the node id already exists the node will not be added
        """
        node = NodeData(node_id,pos)
        self.Nodes[node_id] =node
        self.Edges[node_id]={}
        self.Edges_In[node_id]={}
        self.mc +=1
        return True
        raise NotImplementedError

    def remove_node(self, node_id: int) -> bool:
        """
        Removes a node from the graph.
        @param node_id: The node ID
        @return: True if the node was removed successfully, False o.w.
        Note: if the node id does not exists the function will do nothing
        """
        # check if key exists in dictionary by checking if get() returned default value
        if len(self.Edges[node_id])!=0:
            self.edgeSize -=len(self.Edges[node_id])
            del self.Edges[node_id]
            del self.Edges_In[node_id]
        #should do iteration on every node and check if this node_id is also neighbor there
        for key, value in self.Edges.items():
            if node_id in value:
                self.edgeSize -= 1
                del value[node_id]
        del self.Nodes[node_id]
        self.mc +=1
        return True
        raise NotImplementedError

    def remove_edge(self, node_id1: int, node_id2: int) -> bool:
        """
        Removes an edge from the graph.
        @param node_id1: The start node of the edge
        @param node_id2: The end node of the edge
        @return: True if the edge was removed successfully, False o.w.
        Note: If such an edge does not exists the function will do nothing
        """
        if self.Edges.get(node_id1, -1) != -1:
            if self.Edges[node_id1].get(node_id2, -1) != -1:
                del self.Edges[node_id1][node_id2]
                del self.Edges_In[node_id2][node_id1]
                self.edgeSize -=1
                self.mc += 1
                return True
        return False
        raise NotImplementedError