using System.Collections;
using System.Collections.Generic;
using UnityEngine;

// ================================================================================
// Main scene BackGround behavior
// ================================================================================

public class Background : MonoBehaviour
{

    // =============================================================================
    // Define class variables
    // =============================================================================

    // -----------------------------------------------------------------------------
    // Self GO (GameObject) to interact with
    private GO go;
    // -----------------------------------------------------------------------------
    // Target the BackGround follow (can only follow one target)
    private GO target;

    // =============================================================================
    // Initialisation
    // =============================================================================
    void Start()
    {
        //set self gameobject instance
        go = new GO(gameObject);

        // look for one specific target to center the BackGround with
        target = new GO(GameObject.FindGameObjectWithTag("Player"));
    }
    // =============================================================================
    // Update is called once per frame
    // =============================================================================
    void LateUpdate()
    {
        // update layer parallaxes backgrounds
        uint layerID = 0;
        foreach (Transform layer in transform)
        {
            float layerOffX = layerID * target.posCen().x / 200;
            Vector2 offset = new Vector2(layerOffX, 0.0f);
            layer.GetComponent<Renderer>().material.mainTextureOffset = offset;
            layerID++;
        }
        // update the camera position
        updatePos();
    }
    // -----------------------------------------------------------------------------
    // Update the position to match the target
    private void updatePos()
    {
        // get the current camera position
        Vector3 pos = go.posCen();
        // update only its X component
        pos.x = target.posCen().x;
        pos.z = -10.0f;
        go.setPos(pos);
    }
}
