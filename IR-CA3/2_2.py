import csv
import networkx

def prank(G, alpha = .85, it = 10):
    if len(G.nodes()) == 0:
        return
    oranks = {}
    nranks = {}
    for node in G.nodes():
        oranks[node] = 1 / len(G.nodes())

    while it > 0:
        for node in G.nodes():
            #reset current pagerank
            nranks[node] = 1 / len(G.nodes())
        for node in G.nodes():
            total = 0
            for edge in G.edges():
                if(edge[1] == node):
                    total += (oranks[edge[0]] / G.out_degree(edge[0]))
            nranks[node] = (alpha * total) + ( 1 - alpha )
        oranks = nranks
        it = it - 1
    return nranks

if __name__ == '__main__':
    
	output_graph = networkx.read_edgelist("spider10k.txt", comments = '#', data = True)
	result = prank(output_graph)

	with open('pr_10k.csv', 'w') as q2_output:
		writer = csv.writer(q2_output)
		for key, value in result.items():
		   writer.writerow([key, value])