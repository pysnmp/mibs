#
# PySNMP MIB module PAN-GLOBAL-REG (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/paloaltonetworks/PAN-GLOBAL-REG-MIB
# Produced by pysmi-1.1.3 at Sun Nov 28 21:25:07 2021
# On host fv-az33-735 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, Unsigned32, ObjectIdentity, Gauge32, IpAddress, iso, enterprises, TimeTicks, MibIdentifier, Counter64, Bits, Integer32, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "Unsigned32", "ObjectIdentity", "Gauge32", "IpAddress", "iso", "enterprises", "TimeTicks", "MibIdentifier", "Counter64", "Bits", "Integer32", "Counter32")
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
mibBuilder.exportSymbols("PAN-GLOBAL-REG", panGlobalRegModule=panGlobalRegModule, panMibs=panMibs, panRoot=panRoot, panModules=panModules, PYSNMP_MODULE_ID=panGlobalRegModule, panReg=panReg, panProductsMibs=panProductsMibs, panSpecificMib=panSpecificMib, panCommonMib=panCommonMib)
