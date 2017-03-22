from random import randint
# -*- coding:Utf-8 -*-


class Noeud:
	def __init__(self, valeur):
		self.gauche = None
		self.droite = None
		self.valeur = valeur
class Arbre:
	def __init__(self):
		self.racine = None
	def getRoot(self):
		return self.root
		
############################# AJOUTER UNE VALEUR ######################################################
	def ajouter_valeur(self, valeur):
		if (self.racine == None):
			self.racine = Noeud(valeur)
		else:
			self._ajouter_valeur(valeur, self.racine)
			
	def _ajouter_valeur(self, valeur, noeud):
		if (valeur <= noeud.valeur):
			if(noeud.gauche != None):
				print ("vers gauche")
				self._ajouter_valeur(valeur, noeud.gauche)
			else:
				print ("ajout a gauche :")
				print valeur
				noeud.gauche = Noeud(valeur)
		else:
			if(noeud.droite != None):
				print ("vers droite")
				self._ajouter_valeur(valeur, noeud.droite)
			else:
				print ("ajout a droite:")
				print valeur
				noeud.droite = Noeud(valeur)
############################## PARCOURS SYMETRIQUE DE L ARBRE ############################################
	def symetrique(self):
		if(self.racine != None):
			print ("Parcours symetrique de l'arbre: ")
			self._symetrique(self.racine)
	
	def _symetrique(self, noeud):
		if(noeud != None):
			self._symetrique(noeud.gauche)
			print str(noeud.valeur)
			self._symetrique(noeud.droite)
############################### TEST SI NOEUD SIMPLE PRESENT ###############################################
	def noeud_simple(self):
		if (self.racine != None):
			return self._noeud_simple(self.racine)
	
	def _noeud_simple (self, noeud):
		if ((noeud.gauche != None and noeud.droite == None) or (noeud.gauche == None and noeud.droite != None)):
			return "Noeud simple detecte" #Un noeud simple a été trouvé, la methode renvoie 1
		if (noeud.gauche != None):
			self._noeud_simple(noeud.gauche)
		if (noeud.droite != None):
			self._noeud_simple(noeud.droite)
		return "pas de Noeud simple" #Retourne 1 si aucun noeud simple n'a été trouvé'
######################## AJOUTER x VALEUR ALEATOIRE ################################################################
	def ajouter_n(self, val):
		tab = []
		for compteur in range(val):
			a = randint(0,val)
			tab.append(a)
			self.ajouter_valeur(a)
		print ("liste ajouter dans l'ordre:")
		print tab
######################### PARCOURS PREFIXE ######################################
	def prefixe(self):
		if(self.racine != None):
			print ("parcours prefixe de l'arbre: '")
			self._prefixe(self.racine)
	def _prefixe(self, noeud):
		if (noeud != None):
			print str(noeud.valeur)
			self._prefixe(noeud.gauche)
			self._prefixe(noeud.droite)
arbretest = Arbre()
arbretest.ajouter_n(10)
arbretest.symetrique()
print arbretest.noeud_simple()
