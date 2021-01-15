from unittest import TestCase
from DiGraph import DiGraph


class TestDiGraph(TestCase):
    def test_v_size(self):
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

        assert gr.v_size()==7

    def test_e_size(self):
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

        assert gr.e_size()==9
        gr.remove_edge(6,3)
        assert gr.e_size()==8
        gr.remove_node(2)
        assert gr.e_size()==6

    def test_get_all_v(self):
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

        nodes = gr.get_all_v()
        assert len(nodes) == 7
        assert isinstance(nodes, dict)
        for i in range(6):
            assert i in nodes.keys()

    def test_all_in_edges_of_node(self):
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

        edge_in = gr.all_in_edges_of_node(0)
        assert 1 in edge_in
        edge_in = gr.all_in_edges_of_node(1)
        assert 0 in edge_in
        edge_in = gr.all_in_edges_of_node(2)
        assert 1 in edge_in
        edge_in = gr.all_in_edges_of_node(3)
        for a in [1,2,6]:
            assert a in edge_in
        edge_in = gr.all_in_edges_of_node(4)
        assert 3 in edge_in
        edge_in = gr.all_in_edges_of_node(5)
        assert 4 in edge_in
        edge_in = gr.all_in_edges_of_node(6)
        assert 4 in edge_in

    def test_all_out_edges_of_node(self):
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

        edge_in = gr.all_out_edges_of_node(0)
        assert 1 in edge_in
        edge_in = gr.all_out_edges_of_node(1)
        for a in [0,2,3]:
            assert a in edge_in
        edge_in = gr.all_out_edges_of_node(2)
        assert 3 in edge_in
        edge_in = gr.all_out_edges_of_node(3)
        assert 4 in edge_in
        edge_in = gr.all_out_edges_of_node(4)
        assert 5 in edge_in
        edge_in = gr.all_out_edges_of_node(5)
        assert edge_in == {}
        edge_in = gr.all_out_edges_of_node(6)
        assert 3 in edge_in
        assert isinstance(edge_in, dict)

    def test_get_mc(self):
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

        mc = gr.get_mc()
        gr.add_node(7)
        assert gr.get_mc()==mc + 1
        gr.remove_node(7)
        assert gr.get_mc()==mc + 2

    def test_add_edge(self):
        gr = DiGraph()
        for n in range(7):
            gr.add_node(n)
        gr.add_edge(0, 1, 1)
        assert 0 in gr.all_in_edges_of_node(1)
        gr.add_edge(1, 0, 1.1)
        assert 1 in gr.all_in_edges_of_node(0)
        gr.add_edge(1, 2, 1.3)
        assert 1 in gr.all_in_edges_of_node(2)
        gr.add_edge(2, 3, 1.1)
        assert 2 in gr.all_in_edges_of_node(3)
        gr.add_edge(1, 3, 10)
        gr.add_edge(4, 5, 12)
        gr.add_edge(3, 4, 22)
        gr.add_edge(4, 6, 3)
        gr.add_edge(6, 3, 18)
        assert not 14 in gr.all_in_edges_of_node(4)

    def test_add_node(self):
        gr = DiGraph()
        for n in range(7):
            gr.add_node(n)
        assert gr.v_size()==7
        gr.add_node(2)
        assert gr.v_size() == 7


    def test_remove_node(self):
        gr = DiGraph()
        for n in range(7):
            gr.add_node(n)
        assert gr.v_size()==7
        for i in range(3):
            gr.remove_node(i)
        assert gr.v_size()==4

    def test_remove_edge(self):
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
        assert gr.e_size()==9
        gr.remove_edge(1,3)
        assert gr.e_size()==8
        gr.remove_node(3)
        assert gr.e_size() == 5
