import { tokens } from './helpers'


const Token = artifacts.require('./Token')
require("@babel/preset-env")
require('chai')
  .use(require('chai-as-promised'))
  .should()

contract('Token', ([deployer, receiver])=> {

const name = 'Fritz Token'
const symbol = 'Fritz'
const decimal = '18'
const totalSupply = tokens(1000000).toString()
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
			result.toString().should.equal(totalSupply.toString())
		})

		it('assigns the total supply to the deployer' , async () => {
			const result = await token.balanceOf(deployer)
			result.toString().should.equal(totalSupply.toString())
		})
	})

	describe('sending tokens', () => {
		it('transfers token balances', async () => {
			let balanceOf
			// balances before transfer
			balanceOf = await token.balanceOf(deployer)
			console.log("deployer balance before transfer" , balanceOf.toString())
			balanceOf = await token.balanceOf(receiver)
			console.log("reciever balance before transfer" , balanceOf.toString())
			
			//transfer
			await token.transfer(receiver, tokens(100), { from: deployer})
			//after transfer

			balanceOf = await token.balanceOf(deployer)
			console.log("deployer balance after transfer" , balanceOf.toString())
			balanceOf = await token.balanceOf(receiver)
			console.log("receiver balance after transfer" , balanceOf.toString())

		})
	})
})