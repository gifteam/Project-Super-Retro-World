using System.Collections;
using System.Collections.Generic;
using UnityEngine;
/*
 * input 2D array of bloc
 *      x times y blocs (not event number) array center in the target position (bloc in the center)
 * bloc = x time y pixel (rect)
 *      value = 0, 1 or -1 (nothing, platform, ennemy)
 * array of neural net 1D array
 *      population size
 * neural net
 *      list of neuron (1 layer) 1D array
 *      neuron  = A input et b output
 *      input = 1 bloc value
 *      output = activation function
 *      input weight = - 1 to 1
 *      output weigth = - 1 to 1
 *      perceptron weigth = -1 to 1
 *      fitness (time the target stay alive)
 *      
 * activation function 1D array
 *      sum of input ==> 0 if <= 0, 1 else
 *      
 * button list 1D array
 *      linked to activation function
 *      
 * breed
 *      sort neural net by fitness
 *      create array, add neural net id N times its fitness
 *      mix the array of id
 *      find pair (differents id) not twice the same pair
 *      the pair create a new neural net (half of each neural net)
 *      loop time the pop required
 *      mutation rate = X% = add 1 link between 1 perceptron to the input of bloc or the activation function
 */
public class NetworkClass : MonoBehaviour {

	// Use this for initialization
	void Start () {
		
	}
	
	// Update is called once per frame
	void Update () {
		
	}
}
