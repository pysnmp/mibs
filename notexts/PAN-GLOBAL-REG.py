#
# PySNMP MIB module PAN-GLOBAL-REG (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/paloaltonetworks/PAN-GLOBAL-REG-MIB
# Produced by pysmi-1.1.8 at Sun Jan 16 15:35:36 2022
# On host fv-az36-128 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
IpAddress, ObjectIdentity, enterprises, Integer32, Counter32, TimeTicks, Unsigned32, Gauge32, iso, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, Counter64, ModuleIdentity, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "ObjectIdentity", "enterprises", "Integer32", "Counter32", "TimeTicks", "Unsigned32", "Gauge32", "iso", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "Counter64", "ModuleIdentity", "Bits")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
panGlobalRegModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 25461, 1, 1, 1))
panGlobalRegModule.setRevisions(('2011-02-09 16:10',))
if mibBuilder.loadTexts: panGlobalRegModule.setLastUpdated('201106271040Z')
if mibBuilder.loadTexts: panGlobalRegModule.setOrganization('Palo Alto Networks')
panRoot = ObjectIdentity((1, 3, 6, 1, 4, 1, 25461))
if mibBuilder.loadTexts: panRoot.setStatus('current')
panReg = ObjectIdentity((1, 3, 6, 1, 4, 1, 25461, 1))
if mibBuilder.loadTexts: panReg.setStatus('current')
panModules = ObjectIdentity((1, 3, 6, 1, 4, 1, 25461, 1, 1))
if mibBuilder.loadTexts: panModules.setStatus('current')
panMibs = ObjectIdentity((1, 3, 6, 1, 4, 1, 25461, 2))
if mibBuilder.loadTexts: panMibs.setStatus('current')
panCommonMib = ObjectIdentity((1, 3, 6, 1, 4, 1, 25461, 2, 1))
if mibBuilder.loadTexts: panCommonMib.setStatus('current')
panSpecificMib = ObjectIdentity((1, 3, 6, 1, 4, 1, 25461, 2, 2))
if mibBuilder.loadTexts: panSpecificMib.setStatus('current')
panProductsMibs = ObjectIdentity((1, 3, 6, 1, 4, 1, 25461, 2, 3))
if mibBuilder.loadTexts: panProductsMibs.setStatus('current')
mibBuilder.exportSymbols("PAN-GLOBAL-REG", panReg=panReg, panCommonMib=panCommonMib, panProductsMibs=panProductsMibs, panMibs=panMibs, panRoot=panRoot, PYSNMP_MODULE_ID=panGlobalRegModule, panGlobalRegModule=panGlobalRegModule, panModules=panModules, panSpecificMib=panSpecificMib)
