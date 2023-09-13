#
# PySNMP MIB module CTRON-ROUTERS-INTERNAL-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/enterasys/CTRON-ROUTERS-INTERNAL-MIB
# Produced by pysmi-1.1.8 at Wed Sep 13 14:55:30 2023
# On host fv-az629-233 platform Linux version 5.15.0-1041-azure by user runner
# Using Python version 3.10.13 (main, Aug 28 2023, 08:28:42) [GCC 11.4.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Bits, iso, ModuleIdentity, Gauge32, TimeTicks, IpAddress, ObjectIdentity, Counter32, MibIdentifier, enterprises, Counter64, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "iso", "ModuleIdentity", "Gauge32", "TimeTicks", "IpAddress", "ObjectIdentity", "Counter32", "MibIdentifier", "enterprises", "Counter64", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "NotificationType")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
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
mibBuilder.exportSymbols("CTRON-ROUTERS-INTERNAL-MIB", nwRtrTemp2=nwRtrTemp2, mibs=mibs, ctNetwork=ctNetwork, nwRouter=nwRouter, nwRtrTemp=nwRtrTemp, nwRtrTemp1=nwRtrTemp1, ctronRouterExp=ctronRouterExp, nwRtrSoftReset=nwRtrSoftReset, ctron=ctron, cabletron=cabletron, ctronExp=ctronExp)
