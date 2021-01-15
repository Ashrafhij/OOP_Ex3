from unittest import TestCase
from GraphAlgo import GraphAlgo
from DiGraph import DiGraph



class TestGraphAlgo(TestCase):
    def test_get_graph(self):
        gr = DiGraph()
        for n in range(7):
            gr.add_node(n)
        gr.add_edge(0, 1, 1)
        gr.add_edge(1, 0, 1.1)
        gr.add_edge(1, 2, 1.3)
        gr.add_edge(2, 3, 1.1)
        gr.add_edge(1, 3, 10)
        gr.add_edge(4, 5, 12)
        gr.add_edge(3, 4, 22)
        gr.add_edge(4, 6, 3)
        gr.add_edge(6, 3, 18)
        graphAlgo = GraphAlgo(gr)
        assert gr is graphAlgo.get_graph()

    def save_load(self):
        gr = DiGraph()
        for n in range(7):
            gr.add_node(n)
        gr.add_edge(0, 1, 1)
        gr.add_edge(1, 0, 1.1)
        gr.add_edge(1, 2, 1.3)
        gr.add_edge(2, 3, 1.1)
        gr.add_edge(1, 3, 10)
        gr.add_edge(4, 5, 12)
        gr.add_edge(3, 4, 22)
        gr.add_edge(4, 6, 3)
        gr.add_edge(6, 3, 18)
        graphAlgo = GraphAlgo(gr)

        # save the graph to a json file
        graphAlgo.save_to_json('graph.json')
        #Define another graph
        graphAlgoCopy = GraphAlgo()
        # load the graph that we saved before
        graphAlgoCopy.load_from_json('graph.json')

        #We should get a copy from the First Graph
        for i in gr.get_all_v().keys():
            assert graphAlgo.get_graph().get_all_v().get(i).key is graphAlgoCopy.get_graph().get_all_v().get(i).key

        #Check MC , Vertices_size , Edge_Size
        assert graphAlgo.get_graph().get_mc() is graphAlgoCopy.get_graph().get_mc()
        assert graphAlgo.get_graph().v_size() is graphAlgoCopy.get_graph().v_size()
        assert graphAlgo.get_graph().e_size() is graphAlgoCopy.get_graph().e_size()

        #Same Edges Both Graphs
        for i in gr.get_all_v().keys():
            graph1_Out = graphAlgo.get_graph().all_out_edges_of_node(i)
            graph2_Out = graphAlgoCopy.get_graph().all_out_edges_of_node(i)
            graph1_In = graphAlgo.get_graph().all_in_edges_of_node(i)
            graph2_In = graphAlgoCopy.get_graph().all_in_edges_of_node(i)
        assert True is graph1_Out==graph2_Out
        assert True is graph1_In == graph2_In

    def test_shortest_path(self):
        gr = DiGraph()
        for n in range(7):
            gr.add_node(n)
        gr.add_edge(0, 1, 1)
        gr.add_edge(1, 0, 1.1)
        gr.add_edge(1, 2, 1.3)
        gr.add_edge(2, 3, 1.1)
        gr.add_edge(1, 3, 10)
        gr.add_edge(4, 5, 12)
        gr.add_edge(3, 4, 22)
        gr.add_edge(4, 6, 3)
        gr.add_edge(6, 3, 18)
        graphAlgo = GraphAlgo(gr)
        Src_Dest = graphAlgo.shortest_path(0, 3)
        assert True is (Src_Dest[0]==3.4)
        ls = [0, 1, 2, 3]
        for i in Src_Dest[1]:
            assert True is (i==ls[i])

    def test_connected_component(self):
        gr = DiGraph()
        for n in range(5):
            gr.add_node(n)
        gr.add_edge(0, 1, 3)
        gr.add_edge(1, 2, 10)
        gr.add_edge(3, 4, 5)

        algo = GraphAlgo(gr)
        assert True is (algo.connected_component(0)==[0,1,2])
        assert True is (algo.connected_component(3) == [3,4])


    def test_connected_components(self):
        gr = DiGraph()
        for n in range(5):
            gr.add_node(n)
        gr.add_edge(0, 1, 3)
        gr.add_edge(1, 2, 10)
        gr.add_edge(3, 4, 5)

        algo = GraphAlgo(gr)
        assert True is (algo.connected_components() == [[0, 1, 2],[3,4]])

    # def test_plot_graph(self):
