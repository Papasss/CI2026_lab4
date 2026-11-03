import heapq

class PriorityQueue:
  """Coda con priorità aggiornabile che gestisce anche i nodi visti e i costi"""

  def __init__(self):
    self._heap = []
    self._counter = 0 
    self.entries = {} 
    self.visited = set()  
    self.g_score = {}  
    self.parent = {}  

  def push(self, state, priority):
    """Inserisce uno stato o ne aggiorna la priorità se troviamo una strada migliore"""
    if state in self.visited:
      return

    if state in self.entries and self.entries[state] <= priority:
      return

    self.entries[state] = priority
    self._counter += 1
    heapq.heappush(self._heap, (priority, self._counter, state))

  def pop(self):
    """Estrae e restituisce lo stato con priorità minima"""
    while self._heap:
      priority, _, state = heapq.heappop(self._heap)

      if state not in self.visited and self.entries.get(state) == priority:
        del self.entries[state]
        self.visited.add(state)
        return state
    return None

  def get(self, state):
    """Restituisce la priorità attuale di uno stato in coda (o None se non presente)."""
    return self.entries.get(state, None)

  def is_empty(self):
    return len(self.entries) == 0