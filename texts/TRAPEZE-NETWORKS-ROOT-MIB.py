#
# PySNMP MIB module TRAPEZE-NETWORKS-ROOT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/juniper/TRAPEZE-NETWORKS-ROOT-MIB
# Produced by pysmi-1.1.0 at Fri Nov 19 14:59:52 2021
# On host fv-az33-360 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, NotificationType, MibIdentifier, Gauge32, Counter32, ModuleIdentity, IpAddress, TimeTicks, Counter64, enterprises, ObjectIdentity, Unsigned32, Bits, iso = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "NotificationType", "MibIdentifier", "Gauge32", "Counter32", "ModuleIdentity", "IpAddress", "TimeTicks", "Counter64", "enterprises", "ObjectIdentity", "Unsigned32", "Bits", "iso")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
trpzRootMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 14525))
trpzRootMib.setRevisions(('2008-05-22 00:08', '2007-11-28 00:07', '2006-04-14 00:06', '2005-01-01 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: trpzRootMib.setRevisionsDescriptions(('v3.1.1: Changed IMPORT of enterprises\n                from RFC1155-SMI to SNMPv2-SMI\n                (this will be published in 7.0 release)', 'v3.0.0: Added subtree for\n                wireless Management Applications specific MIBs\n                (this will be published in 7.0 release)', 'v2.0.5: Revised for 4.1 release', 'v1: initial version, as for 4.0 and older releases',))
if mibBuilder.loadTexts: trpzRootMib.setLastUpdated('200805220008Z')
if mibBuilder.loadTexts: trpzRootMib.setOrganization('Trapeze Networks')
if mibBuilder.loadTexts: trpzRootMib.setContactInfo('Trapeze Networks Technical Support\n\t www.trapezenetworks.com\n\t US:            866.TRPZ.TAC\n\t International: 925.474.2400\n\t support@trapezenetworks.com')
if mibBuilder.loadTexts: trpzRootMib.setDescription("Trapeze Networks Root MIB\n\n\tCopyright 2008 Trapeze Networks, Inc.\n\tAll rights reserved.\n\tThis Trapeze Networks SNMP Management Information Base\n\tSpecification (Specification) embodies Trapeze Networks'\n\tconfidential and proprietary intellectual property.\n\tTrapeze Networks retains all title and ownership in\n\tthe Specification, including any revisions.\n\n\tThis Specification is supplied 'AS IS' and Trapeze Networks\n\tmakes no warranty, either express or implied, as to the use,\n\toperation, condition, or performance of the Specification.")
trpzProducts = MibIdentifier((1, 3, 6, 1, 4, 1, 14525, 1))
trpzTemporary = MibIdentifier((1, 3, 6, 1, 4, 1, 14525, 2))
trpzRegistration = MibIdentifier((1, 3, 6, 1, 4, 1, 14525, 3))
trpzMibs = MibIdentifier((1, 3, 6, 1, 4, 1, 14525, 4))
trpzTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 14525, 5))
trpzMgmtAppMibs = MibIdentifier((1, 3, 6, 1, 4, 1, 14525, 6))
mibBuilder.exportSymbols("TRAPEZE-NETWORKS-ROOT-MIB", trpzRegistration=trpzRegistration, trpzRootMib=trpzRootMib, trpzMibs=trpzMibs, trpzTemporary=trpzTemporary, trpzMgmtAppMibs=trpzMgmtAppMibs, PYSNMP_MODULE_ID=trpzRootMib, trpzProducts=trpzProducts, trpzTraps=trpzTraps)
