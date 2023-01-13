#
# PySNMP MIB module CTRON-ROUTERS-INTERNAL-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/enterasys/CTRON-ROUTERS-INTERNAL-MIB
# Produced by pysmi-1.1.8 at Fri Jan 13 12:04:17 2023
# On host fv-az218-3 platform Linux version 5.15.0-1030-azure by user runner
# Using Python version 3.10.9 (main, Dec  7 2022, 08:16:13) [GCC 11.3.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
IpAddress, Unsigned32, enterprises, TimeTicks, Counter32, Bits, Gauge32, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, NotificationType, ModuleIdentity, MibIdentifier, ObjectIdentity, iso = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "Unsigned32", "enterprises", "TimeTicks", "Counter32", "Bits", "Gauge32", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "NotificationType", "ModuleIdentity", "MibIdentifier", "ObjectIdentity", "iso")
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
mibBuilder.exportSymbols("CTRON-ROUTERS-INTERNAL-MIB", ctron=ctron, ctNetwork=ctNetwork, ctronExp=ctronExp, cabletron=cabletron, nwRtrTemp1=nwRtrTemp1, nwRtrTemp=nwRtrTemp, nwRouter=nwRouter, nwRtrSoftReset=nwRtrSoftReset, ctronRouterExp=ctronRouterExp, mibs=mibs, nwRtrTemp2=nwRtrTemp2)
