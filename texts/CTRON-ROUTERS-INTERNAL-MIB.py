#
# PySNMP MIB module CTRON-ROUTERS-INTERNAL-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/enterasys/CTRON-ROUTERS-INTERNAL-MIB
# Produced by pysmi-1.1.8 at Fri Jan  7 00:19:10 2022
# On host fv-az77-763 platform Linux version 5.11.0-1022-azure by user runner
# Using Python version 3.10.1 (main, Dec 14 2021, 13:12:05) [GCC 9.3.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
TimeTicks, Unsigned32, MibIdentifier, Gauge32, iso, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, enterprises, Integer32, ModuleIdentity, Counter32, Bits, IpAddress, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "Unsigned32", "MibIdentifier", "Gauge32", "iso", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "enterprises", "Integer32", "ModuleIdentity", "Counter32", "Bits", "IpAddress", "NotificationType")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
cabletron = MibIdentifier((1, 3, 6, 1, 4, 1, 52))
mibs = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4))
ctron = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1))
ctronExp = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 2))
ctronRouterExp = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 2, 2))
ctNetwork = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 3))
nwRouter = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2))
nwRtrTemp = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 99))
nwRtrTemp1 = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 99, 2))
nwRtrTemp2 = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 99, 2, 2))
nwRtrSoftReset = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 99, 2, 2, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0))).clone(namedValues=NamedValues(("reset", 0)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nwRtrSoftReset.setStatus('mandatory')
if mibBuilder.loadTexts: nwRtrSoftReset.setDescription('Executes a software reset of the device when reset(0)\n                        is written to this object. This reset does not reload \n                        software from Flash EPROM.')
mibBuilder.exportSymbols("CTRON-ROUTERS-INTERNAL-MIB", mibs=mibs, cabletron=cabletron, ctron=ctron, nwRtrTemp1=nwRtrTemp1, ctronExp=ctronExp, nwRouter=nwRouter, nwRtrSoftReset=nwRtrSoftReset, ctNetwork=ctNetwork, nwRtrTemp2=nwRtrTemp2, nwRtrTemp=nwRtrTemp, ctronRouterExp=ctronRouterExp)
