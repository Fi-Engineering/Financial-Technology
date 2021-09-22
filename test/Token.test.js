const Token = artifacts.require('./Token')
require("@babel/preset-env")
require('chai')
  .use(require('chai-as-promised'))
  .should()

contract('Token', (accounts)=> {

const name = 'Fritz Token'
const symbol = 'Fritz'
const decimal = '18'
const totalSupply = '1000000000000000000000000'
let token

beforeEach(async () => {
	// fetch token from blockchain
	token = await Token.new()
})
	describe('deployment', () => {
		it('tracks the name', async () => {
			// read token name here...
			const result = await token.name() 
			// check that the token name is 'My Name'
			result.should.equal(name)
    })

		it('tracks the symbol' , async () => {
			const result = await token.symbol()
			result.should.equal(symbol)
		})
		it('tracks the decimals' , async () => {
			const result = await token.decimals()
			result.toString().should.equal(decimal)
		})
		it('tracks the total supply' , async () => {
			const result = await token.totalSupply()
			result.toString().should.equal(totalSupply)
		})
	})
})