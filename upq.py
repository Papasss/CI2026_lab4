import heapq

class PriorityQueue:
  """Coda con priorità aggiornabile che gestisce anche i nodi visti e i costi."""

  def __init__(self):
    self._heap = []
    self._counter = 0  # Spareggiatore nel caso due stati abbiano la stessa priorità
    self.entries = {}  # Dizionario: stato -> priorità attuale in coda
    self.visited = set()  # Stati già estratti ed espansi definitivamente
    self.g_score = {}  # Dizionario: stato -> numero di mosse dall'inizio
    self.parent = {}  # Dizionario: stato_figlio -> stato_padre

  def push(self, state, priority):
    """Inserisce uno stato o ne aggiorna la priorità se troviamo una strada migliore."""
    if state in self.visited:
      return
    # Se lo stato è già in coda con una priorità migliore o uguale, lo ignoriamo
    if state in self.entries and self.entries[state] <= priority:
      return

    self.entries[state] = priority
    self._counter += 1
    heapq.heappush(self._heap, (priority, self._counter, state))

  def pop(self):
    """Estrae e restituisce lo stato con priorità minima (più promettente)."""
    while self._heap:
      priority, _, state = heapq.heappop(self._heap)
      # Ignora vecchie copie rimaste nello heap dopo un aggiornamento di priorità
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