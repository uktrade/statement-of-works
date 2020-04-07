import React, { useState } from 'react'

import DateField from '@govuk-react/date-field'
import InputField from '@govuk-react/input-field'
import MultiChoice from '@govuk-react/multi-choice'
import TextArea from '@govuk-react/text-area'
import Radio from '@govuk-react/radio'
import Select from '@govuk-react/select'
import Button from '@govuk-react/button'
import FormGroup from '@govuk-react/form-group'
import Fieldset from '@govuk-react/fieldset'
import { ButtonArrow } from '@govuk-react/icons'

const roleData = [
  {
    id: 'DM',
    name: 'Delivery Manager',
  },
  {
    id: 'PM',
    name: 'Product Manager',
  },
  {
    id: 'UR',
    name: 'User Researcher',
  },
  {
    id: 'DEV',
    name: 'Developer',
  },
  {
    id: 'TA',
    name: 'Technical Architect',
  },
  {
    id: 'DES',
    name: 'Designer',
  },
  {
    id: 'UXD',
    name: 'UX Designer',
  },
]

const costCodeData = [
  {
    id: 'STRATEGY',
    name: 'Strategy - 109711',
  },
  {
    id: 'TECH',
    name: 'Technology - 10971',
  },
  {
    id: 'DIGITAL',
    name: 'Digital - 109713',
  },
  {
    id: 'DATA',
    name: 'Data - 109714',
  },
  {
    id: 'DABOPS',
    name: 'DDaT Director and Business Operations - 109715',
  },
  {
    id: 'SPIRE',
    name: 'SPIRE - 109376',
  },
]

const Deliverables = (props) => {
  const { moduleIndex } = props
  const [deliverables, setDeliverables] = useState([{ deliverable: '' }])
  const handleAdd = () => {
    let items = [...deliverables]
    items.push({ deliverables: '' })
    setDeliverables(items)
  }

  const handleRemove = (index) => {
    let items = [...deliverables]
    items.splice(index, 1)
    setDeliverables(items)
  }
  return (
    <div>
      <br />
      <Fieldset>
        <br />
        <Fieldset.Legend size="L">Module {moduleIndex}</Fieldset.Legend>
        <br />
        {deliverables.map((deliverable, index) => (
          <div>
            <TextArea name="module-${moduleIndex}-deliverable-${index}">
              Deliverable {index + 1}
            </TextArea>
            <br />
            <Button onClick={() => handleRemove(index)}>
              Remove deliverable
            </Button>
          </div>
        ))}
        <br />
        <Button onClick={() => handleAdd()}>Add deliverable</Button>&nbsp;
        <DateField
          inputNames={{
            day: 'module-${moduleIndex}-completionDateDay',
            month: 'module-${moduleIndex}-completionDateMonth',
            year: 'module-${moduleIndex}-completionDateYear',
          }}
        >
          Completion date
        </DateField>
      </Fieldset>
    </div>
  )
}

const Modules = () => {
  const [modules, setModules] = useState([1])

  const handleAdd = () => {
    let items = [...modules]
    items.push({ deliverables: '' })
    setModules(items)
  }

  const handleRemove = (index) => {
    let items = [...modules]
    items.splice(index, 1)
    setModules(items)
  }

  return (
    <FormGroup>
      {modules.map((module, index) => (
        <div>
          <Deliverables moduleIndex={index + 1} />
          <br />
          <Button onClick={() => handleRemove(index)}>Remove module</Button>
        </div>
      ))}
      <br />
      <Button onClick={() => handleAdd()}>Add module</Button>&nbsp;
    </FormGroup>
  )
}

const MySelect = (props) => {
  const [options] = useState(props.options)
  const [selectedOption, updateSelectedOption] = useState('')
  const handleChange = (event) => {
    updateSelectedOption(event.target.value)
    if (props.onSelectChange) {
      props.onSelectChange(selectedOption)
    }
  }
  let items = options.map((option) => (
    <option key={option.id} value={option.id}>
      {option.name}
    </option>
  ))
  const { name, label } = props
  return (
    <Select name={name} label={label} onChange={handleChange}>
      {items}
    </Select>
  )
}

const debug = (value) => {
  // TODO: log value
  value
}

const Form = () => {
  const action = (form) => {
    // TODO: submit form
    form
  }

  const onSubmit = (e) => {
    e.preventDefault()
    action(e)
      .then(() => {
        // TODO: add redirect
      })
      .catch((error) => {
        // TODO: log the error
        error
      })
  }

  return (
    <form onSubmit={onSubmit}>
      <InputField name="companyName">Company name</InputField>
      <br />
      <InputField name="slotCode">Slot code</InputField>
      <br />
      <MultiChoice label="Nominated worker">
        <Radio name="nominatedWorker" inline="inline">
          Yes
        </Radio>
        <Radio name="nominatedWorker" inline="inline">
          No
        </Radio>
      </MultiChoice>
      <br />
      <InputField name="hiringManager">Hiring manager</InputField>
      <br />
      <InputField name="team">Team</InputField>
      <br />
      <TextArea name="projectDescription">Project description</TextArea>
      <br />
      <MySelect
        name="role"
        label="Role"
        options={roleData}
        onSelectChange={debug}
      />
      <br />
      <MySelect
        name="costCode"
        label="Cost centre code"
        options={costCodeData}
        onSelectChange={debug}
      />
      <br />
      <InputField name="programmeCode">Programme code</InputField>
      <br />
      <InputField name="projectCode">Project code</InputField>
      <br />
      <DateField
        inputNames={{
          day: 'startDateDay',
          month: 'startDateMonth',
          year: 'startDateYear',
        }}
      >
        Start date
      </DateField>
      <br />
      <DateField
        inputNames={{
          day: 'endDateDay',
          month: 'endDateMonth',
          year: 'endDateYear',
        }}
      >
        End date
      </DateField>
      <br />
      <MultiChoice label="Outside IR35">
        <Radio name="outsideIR35" inline="inline">
          Yes
        </Radio>
        <Radio name="outsideIR35" inline="inline">
          No
        </Radio>
      </MultiChoice>
      <br />
      <InputField name="dailyRate">
        Daily rate [must not include pence or currency symbol, like 126 or 156]
      </InputField>
      <br />
      <Modules />
      <Button icon={<ButtonArrow />} type="submit">
        Generate the document
      </Button>
    </form>
  )
}

export default Form
