using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class CameraClass : MonoBehaviour {

	// Set resolution and we are done here !
	void Start () {
        Screen.SetResolution(640, 480, true, 60);
    }
}
