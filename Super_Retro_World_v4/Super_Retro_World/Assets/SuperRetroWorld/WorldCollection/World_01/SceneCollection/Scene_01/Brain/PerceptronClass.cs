using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Perceptron
{
    public float m_weigth;
    public List<PerceptronInput> m_inputList;
    public List<PerceptronOutput> m_outputList;

    public Perceptron()
    {
        m_inputList = new List<PerceptronInput>();
        m_outputList = new List<PerceptronOutput>();

        m_weigth = Random.Range(-1.0f, 1.0f);
        uint l_inputs = (uint)Mathf.RoundToInt(Random.Range(0.0f, 3.0f));
        for (uint i_inputIndex = 0; i_inputIndex < l_inputs; i_inputIndex++)
        {
            m_inputList.Add(new PerceptronInput());
        }
        uint l_outputs = (uint)Mathf.RoundToInt(Random.Range(0.0f, 3.0f));
        for (uint i_outputIndex = 0; i_outputIndex < l_outputs; i_outputIndex++)
        {
            m_outputList.Add(new PerceptronOutput());
        }
    }
}

public class PerceptronInput
{
    public uint m_blocIndex;
    public float m_weigth;

    public PerceptronInput()
    {
        m_blocIndex = (uint)Mathf.RoundToInt(Random.Range(0.0f, 24.0f));
        m_weigth = Random.Range(-1.0f, 1.0f);
    }
}

public class PerceptronOutput
{
    public uint m_ActiveIndex;
    public float m_weigth;

    public PerceptronOutput()
    {
        m_ActiveIndex = (uint)Mathf.RoundToInt(Random.Range(0.0f, 2.0f));
        m_weigth = Random.Range(-1.0f, 1.0f);
    }
}
