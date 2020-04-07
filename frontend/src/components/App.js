import React from 'react'
import styled from 'styled-components'
import GridRow from '@govuk-react/grid-row'
import GridCol from '@govuk-react/grid-col'

import Main from '@govuk-react/main'

import PageHeader from './PageHeader'
import PhaseBanner from '@govuk-react/phase-banner'
import Footer from '@govuk-react/footer'
import { H1 } from '@govuk-react/heading'

import Form from './Form'

const MyMain = styled(Main)`
  padding-top: 0;
`

const App = () => {
  return (
    <div>
      <PageHeader />
      <MyMain>
        <GridRow>
          <GridCol>
            <PhaseBanner level="alpha">
              This is an initial implementation of Statement of Works.
            </PhaseBanner>
          </GridCol>
        </GridRow>
        <GridRow>
          <GridCol>
            <br />
            <H1>Create Statement of Works document</H1>
            <Form />
          </GridCol>
        </GridRow>
      </MyMain>
      <Footer />
    </div>
  )
}

export default App
