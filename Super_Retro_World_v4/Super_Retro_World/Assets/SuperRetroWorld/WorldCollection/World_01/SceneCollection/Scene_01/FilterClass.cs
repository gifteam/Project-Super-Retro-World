using System.Collections;
using System.Collections.Generic;
using UnityEngine;

// =============================================================================
// Moving filter class
// =============================================================================
public class FilterClass : MonoBehaviour {

    // =============================================================================
    // Class variable
    // =============================================================================
    // GO variables
    private GO m_go;
    private GO m_target;
    private GO m_mask;
    private GO m_maskParent;
    // Instanciation public variables
    public float m_minDistInstanciate;
    public Vector2 m_lastTargetPos;
    public float m_currentDistToTarget;
    // Geometric private variable
    public float angle;

    // =============================================================================
    // Use this for initialization
    // =============================================================================
    void Start () {
        // set GO instance
        m_go = new GO(gameObject);
        m_target = new GO(GameObject.FindWithTag("Player"));
        m_mask = new GO(GameObject.FindWithTag("FilterMask"));
        m_maskParent = new GO(GameObject.Find("[Masks]"));
        // set instanciation variables
        m_minDistInstanciate = 1;
        m_lastTargetPos.x = -100;
        m_lastTargetPos.y = -100;
    }

    // =============================================================================
    // Update is called once per frame
    // =============================================================================
    void Update () {
        //move filter according to target position
        m_go.setPos(m_target.posCen());
        //check if the target has moved enough to instanciate a new mask
        m_currentDistToTarget = m_go.getDistSquared(m_lastTargetPos);
        if (m_currentDistToTarget >= m_minDistInstanciate)
        {
            //instanciate mask
            Instantiate(m_mask.getGO(), m_go.posToV3(m_target.posCen()), Quaternion.identity, m_maskParent.getGO().transform);
            //save new target position
            m_lastTargetPos = m_target.posCen();
        }
    }
}
