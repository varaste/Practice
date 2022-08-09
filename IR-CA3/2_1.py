import networkx 

def deadlock(Graph):
    end_nods = []
    deadlock = {}

    for par_node in Graph.nodes:
        par_node_neighbors = len(list(networkx.neighbors(Graph,par_node)))
        if par_node_neighbors != 1:
            deadlock[par_node] = False
        else:
            deadlock[par_node] = True
            end_nods.append(par_node)
            
    local_edges = {}
    for node in Graph.nodes:
        local_edges[node] = list(networkx.neighbors(Graph,node))

    for node in end_nods:
        continue_to_crawl = True 
        current_node = node 
        while continue_to_crawl:
            if deadlock[current_node] == True and len(local_edges[current_node]) == 1:
                next_node = local_edges[current_node][0] 
                deadlock[next_node] = True  
                del local_edges[current_node] 
                local_edges[next_node].remove(current_node) 
                current_node = next_node
            elif len(local_edges[current_node]) > 1:
                break
    print(deadlock)

if __name__ == '__main__':
    inputgraph = networkx.read_edgelist("spider10k.txt", comments='#', delimiter=None, create_using=None, nodetype=None,
                               data=True, edgetype=None, encoding='utf-8')
    deadlock(inputgraph)


